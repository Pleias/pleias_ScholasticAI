from FlagEmbedding import BGEM3FlagModel
from typing import List, Optional, Union
import numpy as np
from sqlite_vec import serialize_float32

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
            cache_dir="Models",
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


if __name__ == "__main__":
    query = ["That is a happy person"]
    embedded_query = embed_query(query)
    print(embedded_query)
    print(format_for_vec_db(embedded_query[0]))
