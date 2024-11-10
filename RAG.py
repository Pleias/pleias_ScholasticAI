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
    
    # Create temporary table for FTS search
    
    cursor.execute("drop table if exists fts_chunks")
    cursor.execute("""
            create virtual table fts_chunks using fts5(
                text,
                content='chunks', content_rowid='chunk_id'
                )
            """
            )
    cursor.execute("""
            insert into fts_chunks(rowid, text)
            select chunk_id, text
            from chunks
            """)
    cursor.execute("insert into fts_chunks(fts_chunks) values('optimize')")
                    
    query = f"""
        -- extract list of possible chunks from documents
        with list_of_possible_chunks as (
            select chunk_id, 
                document_id 
            from chunks
            where document_id in (:documents)
        ),
        
        -- the sqlite-vec KNN vector search results
        vec_matches as (
        select
            chunk_id,
            row_number() over (order by distance) as rank_number,
            distance
        from chunk_embeddings
        where
            embedding match :embedded_query
            and chunk_id in (select chunk_id from list_of_possible_chunks)
            and k = :k
        ),
        
        -- the FTS5 search results
        fts_matches as (
        select
            rowid,
            row_number() over (order by rank) as rank_number,
            rank as score
        from fts_chunks
        where 
            text match :query
            and rowid in (select chunk_id from list_of_possible_chunks)
        limit :k
        ),
        
        -- combine FTS5 + vector search results with RRF
        final as (
        select
            chunks.chunk_id,
            chunks.text,
            vec_matches.rank_number as vec_rank,
            fts_matches.rank_number as fts_rank,
            -- RRF algorithm
            (
            coalesce(1.0 / (:rrf_k + fts_matches.rank_number), 0.0) * :weight_fts +
            coalesce(1.0 / (:rrf_k + vec_matches.rank_number), 0.0) * :weight_vec
            ) as combined_rank,
            vec_matches.distance as vec_distance,
            fts_matches.score as fts_score
        from fts_matches
        full outer join vec_matches on vec_matches.chunk_id = fts_matches.rowid
        join chunks on chunks.chunk_id = coalesce(fts_matches.rowid, vec_matches.chunk_id)
        order by combined_rank desc
        )
        
        select * from final
    """
    document_string = ', '.join(str(element) for element in documents)
    
    cursor.execute(query, 
                        {
                        'documents': document_string,
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
        query ="test"
        documents = [1, 2, 3]
        results = retrieve_augmented_generation(connection, embedded_query, query, documents)
        print(results)
