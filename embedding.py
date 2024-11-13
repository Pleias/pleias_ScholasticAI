from FlagEmbedding import BGEM3FlagModel
from typing import List, Optional
import struct

embedding_model: Optional[BGEM3FlagModel] = None

def embed_query(query: List[str]) -> List[List[float]]:
    global embedding_model
    # Initialize the model only once when the function is called for the first time
    if embedding_model is None:
        print("Initializing the model...")
        embedding_model = BGEM3FlagModel(
            'BAAI/bge-m3',
            use_fp16=True,
            device="cpu",
            cache_dir="C:/Users/User/Documents/Models"
        )
        
    return embedding_model.encode(query,
                        return_dense=True,
                        return_colbert_vecs=False,
                        return_sparse=False,
                        batch_size=10)['dense_vecs']
    
def serialize_f32(vector: List[float]) -> bytes:
    """serializes a list of floats into a compact "raw bytes" format"""
    return struct.pack("%sf" % len(vector), *vector)


if __name__ == "__main__":
    query = ["That is a happy person"]
    embedded_query = embed_query(query)
    print(embedded_query)
    print(serialize_f32(embedded_query[0]))