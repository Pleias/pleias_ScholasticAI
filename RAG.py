import sqlite3
import sqlite_vec

def embed_query(query, model):
    # to fill with actual embedding query
    return model(query)

# Edit to match actual database schema!!!

def retrieve_augmented_generation(cursor, query, model, documents, k=10, rrf_k=60, weight_fts=1.0, weight_vec=1.0):
    # Retrieve using hybrid search with RRF
    cursor.execute("""
        -- extract chunks from relevant documents      
        with chunk_sentences as (
            select chunk_id, sentence, document_id 
            from chunks
            where document_id in :documents
        ),
        
        -- reconcilate chunks with their embeddings
        sentences_and_embeddings as (
            select s.chunk_id, s.sentence, e.embedding
            from chunk_sentences s
            left join chunk_embeddings e on s.chunk_id = e.chunk_id
        ),
                   
        -- the sqlite-vec KNN vector search results
        with vec_matches as (
        select
            chunk_id,
            row_number() over (order by distance) as rank_number,
            distance
        from sentences_and_embeddings
        where
            embedding match :query_embedding
            and k = :k
        ),
        
        -- the FTS5 search results
        fts_matches as (
        select
            rowid,
            row_number() over (order by rank) as rank_number,
            rank as score
        from fts_chunks
        where sentence match :query
        limit :k
        ),
        
        -- combine FTS5 + vector search results with RRF
        final as (
        select
            sentences_and_embeddings.chunk_id,
            sentences_and_embeddings.sentence,
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
        full outer join vec_matches on vec_matches.article_id = fts_matches.rowid
        join sentences_and_embeddings on sentences_and_embeddings.chunk_id = coalesce(fts_matches.chunk_id, vec_matches.chunk_id)
        order by combined_rank desc
        )
        
        select * from final
        """, 
        {
        'query_embedding': embed_query(query, model),  
        'documents': documents, # Pass the list of document ids
        'k': k,
        'rrf_k': rrf_k,
        'weight_fts': weight_fts,
        'weight_vec': weight_vec
    })
    
    # Fetch and return results
    results = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    return [dict(zip(columns, row)) for row in results]
