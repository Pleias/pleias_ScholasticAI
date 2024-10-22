import json
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.llms.llamafile import Llamafile
import httpx
from openai import OpenAI


def get_response(user_input, debug=False):
    if debug:
        return ["reference"], f"{len(user_input)} This is model answer"
    else:
        return get_answer_from_user_input(user_input)


def get_answer_from_user_input(user_input):
    bm25_retriever = BM25Retriever.from_persist_dir("data/bm25_retriever")
    retrieved_nodes = bm25_retriever.retrieve(user_input)
    prompt = create_prompt(context=retrieved_nodes[0].text, user_query=user_input)
    llm = Llamafile(temperature=0, seed=0, timeout=120_0000)
    resp = llm.complete(prompt).text
    return [retrieved_nodes[0].metadata['file_name']], resp


def create_prompt(context, user_query):
    system = "You are an Q&A assistant, answer the user question given the following context"
    user_query = "Question: " + user_query
    return "\n".join([system, context, user_query])


def get_answer(user_input="Hi, tell me a joke"):
    bm25_retriever = BM25Retriever.from_persist_dir("data/bm25_retriever")
    retrieved_nodes = bm25_retriever.retrieve(user_input)
    prompt = create_prompt(context=retrieved_nodes[0].text, user_query=user_input)
    server_url = "http://127.0.0.1:8080/completion"
    data = {
        "prompt": prompt,
        "stream": False
    }
    try:
        response = httpx.post(server_url, json=data, timeout=100_000_000.0)
        response.raise_for_status()
        print("OK")
        with open('tmp.json', 'w') as f:
            json.dump(response.json(), f, indent=4)

        return response.json()['content']

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except httpx.RequestError as e:
        print(f"Request error occurred: {e}")


def get_open_ai_answer(user_input="Hi, tell me a joke"):
    bm25_retriever = BM25Retriever.from_persist_dir("data/bm25_retriever")
    retrieved_nodes = bm25_retriever.retrieve(user_input)
    retrieved_context = retrieved_nodes[0].text
    prompt = "\n".join([retrieved_context, "Question: " + user_input])

    client = OpenAI(
        base_url="http://localhost:8080/v1",  # base_url="http://localhost:8080/v1",
        api_key="sk-no-key-required"
    )
    completion = client.chat.completions.create(
        model="LLaMA_CPP",
        messages=[
            {"role": "system",
             "content": "You are an Q&A assistant, answer the user question given the following context"},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message


if __name__ == "__main__":
    user_input = "Hi, tell me a joke"
    print(get_answer(user_input))
