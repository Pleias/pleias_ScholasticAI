from FlagEmbedding import BGEM3FlagModel
from typing import List, Optional, Union
import numpy as np
from sqlite_vec import serialize_float32
import random
import string
import time

embedding_model: Optional[BGEM3FlagModel] = None


def embed_query(query: List[str]) -> List[List[float]]:
    global embedding_model
    # Initialize the model only once when the function is called for the first time
    if embedding_model is None:
        print("Initializing the model...")
        embedding_model = BGEM3FlagModel(
            "BAAI/bge-m3",
            use_fp16=True,
            device="cpu",
            cache_dir=r"C:\Users\User\Documents\Models",  # REMOVE
        )

    return embedding_model.encode(
        query,
        return_dense=True,
        return_colbert_vecs=False,
        return_sparse=False,
        batch_size=10,
    )["dense_vecs"]


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

def generate_random_sentences(
    num_sentences: int = 60, max_length: int = 1000
) -> List[str]:
    return [generate_random_sentence(max_length) for _ in range(num_sentences)]


if __name__ == "__main__":
    start_time = time.time()
    sentences = generate_random_sentences()
    embedded_query = embed_query(sentences)
    end_time = time.time()
    print(embedded_query[:20])
    print(f"Time taken to run the script: {end_time - start_time} seconds")
    print(f"Time taken per query: {(end_time - start_time) / len(sentences)} seconds")