import requests
import time
import json
import re
from connect_db import ConnectDB
from RAG import retrieve


def construct_prompt(results, user_message):
    # hash_ids = ['**7b3a9c2d4e8f5g1h**', '**9d4e2f7c8b5a3h1i**']
    text_chunks = [res['text'] for res in results]
    titles = [res['title'] for res in results]
    sources = ''
    for i in range(len(text_chunks)):
        source = "\n".join([titles[i], text_chunks[i]])  # hash_ids[i],
        sources += source

    prompt = f"""### Query ###\n{user_message}\n\n### Source ###\n{sources}\n\n### Analysis ###\n"""
    return prompt


def generate_with_llamafile_api(prompt):
    data = {
        "n_predict": 1000,  # Predictions slider (max tokens)
        "temperature": 0.25,  # Temperature slider
        "repeat_penalty": 1.0,  # Penalize repeat sequence slider
        "repeat_last_n": 256,  # Consider N last tokens for penalize slider
        "top_k": 40,  # Top-K sampling slider
        "top_p": 0.95,  # Top-P sampling slider
        "min_p": 0.05,  # Min-P sampling slider
        "tfs_z": 1,  # Tail-free sampling parameter, reduces the impact of low-probability tokens
        "typical_p": 1,  # Controls how "typical" the sampling should be (1 means standard sampling)
        "presence_penalty": 0.2,  # penalty for tokens that have appeared at all
        "frequency_penalty": 0.2,  # penalty based on how frequently tokens have appeared
        "mirostat": 0,  # "no Mirostat" radio option
        "mirostat_tau": 5,  # Mirostat target complexity (only if mirostat enabled)
        "mirostat_eta": 0.1,  # Mirostat learning rate (only if mirostat enabled)
        "n_probs": 0,  # Show Probabilities slider
        "min_keep": 0,  # Mkeep minimum number of candidates per sampling
        "stop": ["#END#"],
        "stream": True,
        "prompt": prompt,
        "cache_prompt": False,
        "slot_id": 0
    }

    headers = {
        'Accept': 'text/event-stream',
        'Content-Type': 'application/json'
    }

    try:
        print("Sending request...")
        start_time = time.time()

        response = requests.post(
            'http://127.0.0.1:8080/completion',
            json=data,
            headers=headers,
            stream=False
        )

        print("Receiving response...")
        full_response = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    text = decoded_line[6:]  # Remove 'data: ' prefix
                    if text != '[DONE]':
                        try:
                            json_response = json.loads(text)
                            if 'content' in json_response:
                                content = json_response['content']
                                full_response += content
                        except json.JSONDecodeError:
                            print("Failed to parse JSON:", text)

        end_time = time.time()
        total_time = end_time - start_time

        print(f"\n-------------------")
        print(f"Total time: {total_time:.2f} seconds")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Error type: {type(e)}")

    return full_response


def replace_references(text, ref_map):
    def ref_replacer(match):
        ref_name = re.findall(r'<ref name="[^"]+">', match.group(0))[0]
        replacement = ref_map[ref_name]
        return replacement

    updated_text = re.sub(r'<ref name="[^"]+">[^<]+</ref>', ref_replacer, text)
    return updated_text


def return_span(number=1):
    return f"""<span style="border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;">{number}</span>"""


def convert_input_msg_to_html(answer):
    pattern = r'###\s*Answer\s*###'
    match = re.search(pattern, answer)
    start_answer = match.end()
    end_answer = answer.find("#END#") if answer.find("###") == -1 else len(answer)
    answer = answer[start_answer:end_answer]
    references = re.findall(r'<ref name="[^"]+">', answer)
    ref_map = {}
    reference_count = 1
    for ref in references:
        if ref not in ref_map:
            ref_map[ref] = return_span(reference_count)
            reference_count += 1
    updated_text = replace_references(answer, ref_map)
    return updated_text


def retrive_from_open_alex(user_message):
    return []


def get_response_and_metadata(user_message, open_alex):
    if open_alex:
        results = retrive_from_open_alex(user_message)
    else:
        connection = ConnectDB().connection
        results = retrieve(connection, user_message)

    prompt = construct_prompt(results, user_message)
    raw_response = generate_with_llamafile_api(prompt)
    html_output = convert_input_msg_to_html(raw_response)

    references_info = []
    for reference in results:
        reference_info = {
            "title": reference["title"],
            "author": reference["author"],
            "creation_date": reference["creation_date"],
            "source_database": reference["source_database"],
        }
        references_info.append(reference_info)
    return references_info, html_output
