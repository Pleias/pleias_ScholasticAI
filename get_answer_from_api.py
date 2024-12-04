import requests
import time
import json
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
    full_response = None
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
        "slot_id": 0,
    }

    headers = {"Accept": "text/event-stream", "Content-Type": "application/json"}

    try:
        print("Sending request...")
        start_time = time.time()

        response = requests.post(
            "http://127.0.0.1:8080/completion", json=data, headers=headers, stream=False
        )

        print("Receiving response...")
        full_response = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith("data: "):
                    text = decoded_line[6:]  # Remove 'data: ' prefix
                    if text != "[DONE]":
                        try:
                            json_response = json.loads(text)
                            if "content" in json_response:
                                content = json_response["content"]
                                full_response += content
                        except json.JSONDecodeError:
                            print("Failed to parse JSON:", text)

        end_time = time.time()
        total_time = end_time - start_time

        print("\n-------------------")
        print(f"Total time: {total_time:.2f} seconds")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Error type: {type(e)}")

    return full_response


def return_span(number=1, source="blue"):
    """Create a reference number styled consistently"""
    return f"""<span class="marker {source}">{number}</span>"""


def get_author_html(author):
    return f"""
<html>
    <head>
        <style>
            .authors {{
                margin-left: 20px;
                font-family: "SF Pro", sans-serif;
                font-size: 12px;
                font-weight: 400;
                line-height: 14.32px;
                text-align: left;
                text-underline-position: from-font;
                text-decoration-skip-ink: none;
                color: #828282;
            }}
        </style>
    </head>
    <body>
        <span class="authors">{author}</span>
    </body>
</html>
"""


def get_title_html(title):
    return f"""
<html>
    <head>
        <style>
            .title {{
                font-family: "SF Pro", sans-serif;
                font-size: 14px;
                font-weight: 400;
                line-height: 22px;
                letter-spacing: -0.43px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <span class="title">{title}</span>
    </body>
</html>
"""


def get_html(answer):
    return f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transformers Architecture</title>
    <style>
      body {{
        font-family: SF Pro;
        font-size: 16px;
        font-weight: 400;
        line-height: 22px;
        letter-spacing: -0.4300000071525574px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
      }}
      .marker {{
        width: 16px;
        height: 18px;
        padding: 0px 2px;
        justify-content: center;
        align-items: center;
        border-radius: 3px;
        text-decoration: none;
      }}
      .blue {{
        color: #042FF4;
        font-family: SF Pro;
        font-size: 12px;
        font-style: normal;
        font-weight: 200;
        line-height: normal;
        background: #BFEFFF;
      }}
      .yellow {{
        color: #B66400;
        font-family: SF Pro;
        font-size: 12px;
        font-weight: 200;
        line-height: 14.32px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        background: #FFE289;
     .green {{
        color: #e0f8d6;
        font-family: SF Pro;
        font-size: 12px;
        font-weight: 200;
        line-height: 14.32px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        background: #afed95;
      }}
     .pink {{
        color: #9d6f7d;
        font-family: SF Pro;
        font-size: 12px;
        font-weight: 200;
        line-height: 14.32px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        background: #d7c5cb;
      }}
    </style>
  </head>
  <body>
    <p>{answer}</p>
  </body>
</html>
"""


def convert_input_msg_to_html(answer):
    """
    Converts <ref name="X">"content"</ref> into clickable links
    Fully compatible with ReferenceWidget's expected format
    """
    import re

    # Track reference numbers
    ref_count = 1
    ref_map = {}
    sources = ["blue", "yellow", "green", "pink"]

    def replace_ref(match):
        nonlocal ref_count
        ref_name = match.group(1)  # Gets "96" from name="96"
        ref_content = match.group(2)  # Gets the quoted text

        ref_content = ref_content.strip('"')

        if ref_name in ref_map:
            source = ref_map[ref_name]
        else:
            source_id = len(ref_map)
            if source_id < len(sources):
                source = sources[source_id]
                ref_map[ref_name] = source
            else:
                source = sources[-1]
        return f'<a href="{ref_name}:{ref_content}" class="marker {source}">{ref_count}</a>'

    # Match exactly: <ref name="96">"content"</ref>
    pattern = r'<ref name="([^"]+)">"([^"]+)"</ref>'

    # Process each match
    last_end = 0
    final_text = ""
    for match in re.finditer(pattern, answer):
        # Add text before this match
        final_text += answer[last_end : match.start()]
        # Add the replacement
        final_text += replace_ref(match)
        last_end = match.end()
        ref_count += 1

    # Add any remaining text
    final_text += answer[last_end:]
    ans_start = final_text.find("<|answer_start|>")
    if ans_start == -1:
        return final_text
    else:
        return final_text[ans_start + len("<|answer_start|>") :]


def retrieve_from_open_alex(user_message):
    r = OpenAlexReader()
    results = r.retrieve_from_open_alex(user_query=user_message, max_results=3)
    return results


def get_response_and_metadata(user_message, open_alex):
    if open_alex:
        results = retrieve_from_open_alex(user_message)
    else:
        connection = ConnectDB().connection
        results = retrieve(connection, user_message)
    prompt = construct_prompt(results, user_message)
    raw_response = generate_with_llamafile_api(prompt)

    # Convert to HTML with only reference formatting
    html_output = convert_input_msg_to_html(raw_response)

    # Prepare reference information for tooltips
    references_info = []
    for result in results:
        references_info.append(
            {
                "title": result.get("title", "Unknown Title"),
                "author": result.get("author", "Unknown Author"),
                "creation_date": result.get("creation_date", "Unknown Date"),
                "source_database": result.get("source_database", "local"),
                "document_id": result.get("document_id", "Unknown document id"),
                "chunk_id": result.get("chunk_id", "Unknown chunk id"),
            }
        )

    return references_info, html_output
