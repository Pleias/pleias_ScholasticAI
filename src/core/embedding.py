from typing import List, Optional, Union
import numpy as np
from sqlite_vec import serialize_float32
import random
import string
from sentence_transformers import SentenceTransformer


embedding_model: Optional[SentenceTransformer] = None


def embed_query(query: List[str]) -> List[List[float]]:
    global embedding_model
    if embedding_model is None:
        print("Initializing the model...")
        embedding_model = SentenceTransformer(
            model_name_or_path= "intfloat/multilingual-e5-small",
            device="cpu",
            cache_folder = "models", #r"C:\Users\User\Documents\Models",
        )
    print("Embedding...")
    return embedding_model.encode(
        query
    )


def format_for_vec_db(vector: Union[List[float], np.ndarray]):
    """Makes sure the object is valid to be stored in the SQLite-vec database.
    If it is a list of floats, converts it into a compact "raw bytes" format."""
    if isinstance(vector, np.ndarray):
        return vector.astype(
            np.float32
        )  # Nothing to do as np implements Buffer Protocol
    elif isinstance(vector, list):
        return serialize_float32(vector)
    else:
        raise TypeError("Unsupported type. Expected a numpy array or a list.")

def generate_random_sentence(max_length: int = 1000) -> str:
    length = random.randint(1, max_length)
    return "".join(
        random.choices(string.ascii_letters + string.digits + " ", k=length)
    )


if __name__ == "__main__":
    import time
    
    def generate_random_sentences(
        num_sentences: int = 100, max_length: int = 1000
    ) -> List[str]:
        return [generate_random_sentence(max_length) for _ in range(num_sentences)]
    queries = [
    "What are some ways to reduce stress?",
    "What are the benefits of drinking green tea?",
    ]

    start_time = time.time()
    sentences = generate_random_sentences()
    embedded_query = embed_query(sentences)
    end_time = time.time()
    print(embed_query(queries).shape)
    print(f"Time taken to run the script: {end_time - start_time} seconds")
    print(f"Query per second: {len(sentences) / (end_time - start_time)} seconds")