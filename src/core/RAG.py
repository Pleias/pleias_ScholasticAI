from src.core.embedding import embed_query, format_for_vec_db
from typing import List, Optional


def retrieve(
    connection,
    query: str,
    documents: Optional[List] = None,
    k: int = 2,
    rrf_k: float = 10,
    weight_fts: float = 1.0,
    weight_vec: float = 1.0,
    final_k: int = 3,
):
    """
    Retrieve relevant document chunks based on a query using hybrid search (combination of vector search and full-text search (FTS)).
    Arguments:
        connection: The database connection object.
        query (str): The search query string.
        documents (Optional[List]): A list of document IDs to restrict the search to specific documents. Defaults to None for search in all documents.
        k (int): The number of top results to return from each search method (vector search and FTS). Defaults to 2.
        rrf_k (float): The rank fusion parameter for Reciprocal Rank Fusion (RRF). Defaults to 10.
        weight_fts (float): The weight for the FTS ranking in the combined rank. Defaults to 1.0.
        weight_vec (float): The weight for the vector search ranking in the combined rank. Defaults to 1.0.
        final_k (int): The final number of top results to return after combining both methods. Defaults to 3.
    Returns:
        List[Dict]: A list of dictionaries containing the top 3 combined search results.
    """
    cursor = connection.cursor()

    # We need to first extract the list of possible chunks from the documents
    cursor.execute("DROP TABLE IF EXISTS temp_list_of_possible_chunks;")

    if documents is not None:
        placeholders = ", ".join("?" for _ in documents)
        create_temp_table_query = f"""
            CREATE TEMP TABLE temp_list_of_possible_chunks AS
            WITH list_of_possible_chunks AS (
                SELECT chunk_id, document_id 
                FROM chunks
                WHERE document_id IN ({placeholders})
            )
            SELECT * FROM list_of_possible_chunks;
        """
        cursor.execute(create_temp_table_query, documents)
    else:
        create_temp_table_query = """
            CREATE TEMP TABLE temp_list_of_possible_chunks AS
            WITH list_of_possible_chunks AS (
                SELECT chunk_id, document_id 
                FROM chunks
            )
            SELECT * FROM list_of_possible_chunks;
        """
        cursor.execute(create_temp_table_query)

    embedded_query = embed_query(query)

    main_rag_query = """
        -- SQLite-vector KNN vector search results
        WITH vec_matches AS (
            SELECT
                chunk_id,
                ROW_NUMBER() OVER (ORDER BY distance) AS rank_number,
                distance
            FROM chunk_embeddings
            WHERE
                embedding MATCH :embedded_query
                AND chunk_id IN (SELECT chunk_id FROM temp_list_of_possible_chunks)
                AND k = :k
        ),

        -- FTS5 search results
        fts_matches AS (
            SELECT
                rowid,
                ROW_NUMBER() OVER (ORDER BY rank) AS rank_number,
                rank AS score
            FROM chunks_fts
            WHERE 
                text MATCH :query
                AND rowid IN (SELECT chunk_id FROM temp_list_of_possible_chunks)
            LIMIT :k
        ),

        -- Combine FTS5 and vector search results with RRF
        ranking_query AS (
            SELECT
                chunks.chunk_id,
                chunks.document_id,
                pdf_metadata.title,
                pdf_metadata.author,
                pdf_metadata.creation_date,
                chunks.text,
                vec_matches.rank_number AS vec_rank,
                fts_matches.rank_number AS fts_rank,
                -- RRF algorithm
                (
                    COALESCE(1.0 / (:rrf_k + fts_matches.rank_number), 0.0) * :weight_fts +
                    COALESCE(1.0 / (:rrf_k + vec_matches.rank_number), 0.0) * :weight_vec
                ) AS combined_rank,
                vec_matches.distance AS vec_distance,
                fts_matches.score AS fts_score
            FROM fts_matches
            FULL OUTER JOIN vec_matches ON vec_matches.chunk_id = fts_matches.rowid
            JOIN chunks ON chunks.chunk_id = COALESCE(fts_matches.rowid, vec_matches.chunk_id)
            LEFT JOIN pdf_metadata ON pdf_metadata.id = chunks.document_id
        )
        
        SELECT * FROM ranking_query
        ORDER BY combined_rank DESC
        LIMIT :final_k"""

    cursor.execute(
        main_rag_query,
        {
            "embedded_query": format_for_vec_db(embedded_query),
            "query": query.replace("?", ""),
            "k": k,
            "rrf_k": rrf_k,
            "weight_fts": weight_fts,
            "weight_vec": weight_vec,
            "final_k": final_k,
        },
    )

    results = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    return [dict(zip(columns, row)) for row in results]
