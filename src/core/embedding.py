from typing import List, Optional, Union
import numpy as np
from sqlite_vec import serialize_float32
import random
import string

from sentence_transformers import SentenceTransformer

# https://huggingface.co/dunzhang/stella_en_400M_v5

query_prompt_name = "s2p_query" # sentence to passage because we compare sentences to passages
queries = [
    "What are some ways to reduce stress?",
    "What are the benefits of drinking green tea?",
]

embedding_model: Optional[SentenceTransformer] = None


# query_embeddings = embedding_model.encode(queries, prompt_name=query_prompt_name)
# doc_embeddings = embedding_model.encode(docs)
# print(query_embeddings.shape, doc_embeddings.shape)
# # (2, 1024) (2, 1024)

# similarities = embedding_model.similarity(query_embeddings, doc_embeddings)
# print(similarities)
# # tensor([[0.8398, 0.2990],
# #         [0.3282, 0.8095]])




def embed_query(query: List[str]) -> List[List[float]]:
    global embedding_model
    # Initialize the model only once when the function is called for the first time
    if embedding_model is None:
        print("Initializing the model...")
        embedding_model = SentenceTransformer(
            model_name_or_path= "intfloat/multilingual-e5-small",
            # trust_remote_code=True, for stella only
            device="cpu",
            cache_folder = r"C:\Users\User\Documents\Models",
            config_kwargs={"use_memory_efficient_attention": False, 
                           "unpad_inputs": False},
            # max_tokens=512
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

def generate_random_sentences(
    num_sentences: int = 100, max_length: int = 1000
) -> List[str]:
    return [generate_random_sentence(max_length) for _ in range(num_sentences)]


if __name__ == "__main__":
    # start_time = time.time()
    # sentences = generate_random_sentences()
    # embedded_query = embed_query(sentences)
    # end_time = time.time()
    print(embed_query(queries).shape)
    # print(f"Time taken to run the script: {end_time - start_time} seconds")
    # print(f"Query per second: {len(sentences) / (end_time - start_time)} seconds")