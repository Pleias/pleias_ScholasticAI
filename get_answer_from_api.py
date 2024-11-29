import requests
import time
import json
import re
from connect_db import ConnectDB
from RAG import retrieve
from open_alex_retrieval import OpenAlexReader


def construct_prompt(results, user_message):
    """
    Constructs a prompt with specific XML-style tags for LLM formatting
    """
    prompt = f"<|query_start|>{user_message}<|query_end|>\n"
    
    for result in results:
        source = f"<|source_start|><|source_id_start|>{result.get('chunk_id', '')}<|source_id_end|>{result['text']}<|source_end|>\n"
        prompt += source
    
    prompt += "<|source_analysis_start|>"
    return prompt


def generate_with_llamafile_api(prompt):
    data = {
        "n_predict": 850,  # Predictions slider (max tokens)
        "temperature": 0,  # Temperature slider
        "repeat_penalty": 1,  # Penalize repeat sequence slider
        "repeat_last_n": 256,  # Consider N last tokens for penalize slider
        "top_k": 40,  # Top-K sampling slider
        "top_p": 0.95,  # Top-P sampling slider
        "min_p": 0.05,  # Min-P sampling slider
        "tfs_z": 1,  # Tail-free sampling parameter, reduces the impact of low-probability tokens
        "typical_p": 1,  # Controls how "typical" the sampling should be (1 means standard sampling)
        "presence_penalty": 0,  # penalty for tokens that have appeared at all
        "frequency_penalty": 0,  # penalty based on how frequently tokens have appeared
        "mirostat": 0,  # "no Mirostat" radio option
        "mirostat_tau": 5,  # Mirostat target complexity (only if mirostat enabled)
        "mirostat_eta": 0.1,  # Mirostat learning rate (only if mirostat enabled)
        "n_probs": 0,  # Show Probabilities slider
        "min_keep": 0,  # Mkeep minimum number of candidates per sampling
        "stop": ["<|answer_end|>"],
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

def return_span(number=1):
    """Create a reference number styled consistently"""
    return (
        f'<a href="{number}" style="color: #007bff; cursor: pointer; text-decoration: none; '
        f'background-color: #e7f3ff; padding: 2px 6px; margin: 0 2px; '
        f'border-radius: 3px; border: 1px solid #007bff;">[{number}]</a>'
    )

def replace_references(text, ref_map):
    def ref_replacer(match):
        ref_text = match.group(0)
        ref_name = re.findall(r'<ref name="([^"]+)">', ref_text)[0]  
        ref_content = re.findall(r'>(.*?)</ref>', ref_text)[0]
        ref_key = f'<ref name="{ref_name}">'
        span = ref_map[ref_key]
        return span

    updated_text = re.sub(r'<ref name="[^"]+">[^<]+</ref>', ref_replacer, text)
    return updated_text

def convert_input_msg_to_html(answer):
    """
    Converts <ref name="X">"content"</ref> into clickable links
    Fully compatible with ReferenceWidget's expected format
    """
    import re
    
    # Track reference numbers
    ref_count = 1
    ref_map = {}
    
    def replace_ref(match):
        nonlocal ref_count
        ref_name = match.group(1)    # Gets "96" from name="96"
        ref_content = match.group(2)  # Gets the quoted text
        
        # Remove the surrounding quotes from content
        ref_content = ref_content.strip('"')
        
        # Create a link that exactly matches what ReferenceWidget expects:
        # - href contains "id:content" format for tooltip
        # - style ensures it's visible and clickable
        return (f'<a href="{ref_name}:{ref_content}" style="color: #007bff; '
                f'text-decoration: none;">[{ref_count}]</a>')

    # Match exactly: <ref name="96">"content"</ref>
    pattern = r'<ref name="([^"]+)">"([^"]+)"</ref>'
    
    # Process each match
    last_end = 0
    final_text = ""
    
    for match in re.finditer(pattern, answer):
        # Add text before this match
        final_text += answer[last_end:match.start()]
        # Add the replacement
        final_text += replace_ref(match)
        last_end = match.end()
        ref_count += 1
    
    # Add any remaining text
    final_text += answer[last_end:]
    
    return final_text



def retrieve_from_open_alex(user_message, debug=True):
    if debug:
        return [
            {"text": "put your text",
             'title': "Short story about Anna", 'author': "Kamu", 'source_database': 'open_alex',
             "creation_date": "01/12/12",
             "document_id" : 1,
             "chunk_id":1},
            {"text": "put your text",
             'title': "Short story about Anna", 'author': "CHUK", 'source_database': 'open_alex',
             "creation_date": "01/12/12",
             "document_id" : 2,
             "chunk_id":2},
            {"text": "put your text",
             'title': "Short story about Anna", 'author': "LION", 'source_database': 'open_alex',
             "creation_date": "01/12/12",
             "doucment_id" : 3,
             "chunk_id":3},
        ]
    else:
        r = OpenAlexReader()
        results = r.retrieve_from_open_alex(user_query=user_message, max_results=3)
        return results


def get_response_and_metadata(user_message, open_alex):
    #print("In get_response_and_metadata")
    if open_alex:
        #print("retrieving from open alex")
        results = retrieve_from_open_alex(user_message)
    else:
        #print("retrieving from local db")
        connection = ConnectDB().connection
        results = retrieve(connection, user_message)

    #print("RESULTS : ",results) 
    prompt = construct_prompt(results, user_message)
    raw_response = generate_with_llamafile_api(prompt)
    
    # Convert to HTML with only reference formatting
    html_output = convert_input_msg_to_html(raw_response)
    
    # Prepare reference information for tooltips
    references_info = []
    for result in results:
        references_info.append({
            "title": result.get("title", "Unknown Title"),
            "author": result.get("author", "Unknown Author"),
            "creation_date": result.get("creation_date", "Unknown Date"),
            "source_database": result.get("source_database", "local"),
            "document_id": result.get("document_id", "Unknown document id"),
            "chunk_id": result.get("chunk_id", "Unknown chunk id")
        })
    
    return references_info, html_output

