import sqlite3
import sqlite_vec
from typing import List
import struct

def embed_query(query, model):
    # to fill with actual embedding query
    return [0.1, 0.0, 0.1, 0.4]
### NOTE: in the end, this should be the same embedding function as in connect_db.py



def serialize_f32(vector: List[float]) -> bytes:
    """serializes a list of floats into a compact "raw bytes" format"""
    return struct.pack("%sf" % len(vector), *vector)

def retrieve_augmented_generation(connection, embedded_query, query, documents, k=10, rrf_k=60, weight_fts=1.0, weight_vec=1.0):
    """
    Retrieve using hybrid search with RRF.
    Example usage:
        from connect_db import ConnectDB
        connection = ConnectDB().connection
        embedded_query = [0.1, 0.2, 0.3, 0.4]
        documents = [1, 2, 3]
        results = retrieve_augmented_generation(connection, embedded_query, documents)
    """
    cursor = connection.cursor()
    
    # We need to first extract the list of possible chunks from the documents
    cursor.execute("DROP TABLE IF EXISTS temp_list_of_possible_chunks;")
    placeholders = ', '.join('?' for _ in documents)
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
            FROM fts_chunks
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
            ORDER BY combined_rank DESC
        )
        
        SELECT * FROM ranking_query"""
    
    cursor.execute(main_rag_query, 
                        {
                            'embedded_query': serialize_f32(embedded_query),
                            'query': query,
                            'k': k,
                            'rrf_k': rrf_k,
                            'weight_fts': weight_fts,
                            'weight_vec': weight_vec
                        }
                     )
    
    # Fetch and return results
    results = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    return [dict(zip(columns, row)) for row in results]



if __name__ == "__main__":
        from connect_db import ConnectDB
        connection = ConnectDB().connection
        embedded_query = [0.1, 0.0, 0.1, 0.4]
        query ="transformer"
        documents = [1, 2, 3]
        results = retrieve_augmented_generation(connection, embedded_query, query, documents)
        print(results)
