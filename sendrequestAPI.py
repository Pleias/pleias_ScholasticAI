import requests
import time
import json

content = """ ### Query ###
What are the main types of risks associated with Large Language Models (LLMs)?

 ### Source ###
**4e2d3c7a186d08a4**
I. INTRODUCTION
Large language models (LLMs) [1]–[5] that own massive model parameters pre-trained on extensive corpora, have catalyzed a revolution in the fields of Natural Language Processing (NLP). The scale-up of model parameters and the expansion of pre-training corpora have endowed LLMs with remarkable capabilities across various tasks, including text generation [2], [4], [5], coding [2], [6], and knowledge reasoning [7]–[10]. Furthermore, alignment techniques (e.g., supervised fine-tuning and reinforcement learning from human feedback [4], [11]) are proposed to encourage LLMs to align their behaviors with human preferences, thereby enhancing the usability of LLMs. In practice, advanced LLM systems like ChatGPT [12] have consistently garnered a global user base, establishing themselves as competitive solutions for complex NLP tasks.

Despite the great success of LLM systems, they may sometimes violate human values and preferences, thus raising concerns about safety and security of LLM-based applications. To mitigate the risks of LLMs, it is imperative to develop a comprehensive taxonomy that enumerates all potential risks inherent in the construction and deployment of LLM systems. This taxonomy is intended to serve as a guidance for evaluating and improving the reliability of LLM systems. Predominantly, the majority of existing efforts [15]–[18] propose their risk taxonomies based on the assessment and analysis of output content with multiple metrics. In general, an LLM system consists of various key modules — an input module for receiving prompts, a language model trained on vast datasets, a toolchain module for development and deployment, and an output module for exporting LLM-generated content. To the best of our knowledge, there have been limited taxonomies proposed to systematically categorize risks across the various modules of an LLM system. Hence this work aims to bridge the gap to encourage LLM participants to 1) comprehend the safety and security concerns associated with each module of an LLM system, and 2) embrace a systematic perspective for building more responsible LLM systems.

generative LMs that generate sequences in an autoregressive manner. Formally, given a sequence of tokens v<t = {v0, v1, v2, · · · , vt−1} and a vocabulary V, the next token vt ∈V is determined based on the probability distribution p (v|v<t). Beam search [25] and greedy search [26] are two classic methods to determine the next token.

**9f6d52c01a14622d**
I. INTRODUCTION
- We propose a module-oriented taxonomy, which attributes a potential risk to specific modules of an LLM system. This taxonomy aids developers in gaining a deeper understanding of the root causes behind possible risks and thus facilitates the development of beneficial LLM systems.

Training Pipeline. LLMs undergo a series of exquisite development steps to implement high-quality text generation. The typical process of LLM development contains three steps — pre-training, supervised fine-tuning, and learning from human feedback [11], [24], [33]–[40]. In what follows, we will briefly review the core steps for training LLMs to help readers understand the preliminary knowledge of LLM construction.

- With a more systematic perspective, our taxonomy covers a more comprehensive range of LLM risks than the previous taxonomies. It is worth noting that we consider the security issues closely associated with the toolchain, which is rarely discussed in prior surveys.

- Pre-Training. The initial LLM is pre-trained on a large-scale corpora to obtain extensive general knowledge. The pre-training corpora is a mixture of datasets from diverse sources, including web pages, books, and user dialog data. Moreover, specialized data, such as code, multilingual data, and scientific data, is incorporated to enhance LLMs's reasoning and task-solving abilities [41]–[44]. For the collected raw data, data pre-processing [2]–[5] is required to remove noise and redundancy. After that, tokenization [45] is used to transform textual data into token sequences for language modeling. By maximizing the likelihood of token sequences, the pre-trained model is empowered with impressive language understanding and generation ability.

Roadmap. The subsequent sections are organized as follows: Section II introduces the background of LLMs. Section III introduces the risks of LLM systems. Section IV offers an overview of the safety and security concerns associated with each module of an LLM system. Section V surveys the mitigation strategies employed by different system modules. Section VI summarizes existing benchmarks for evaluating the safety and security of LLM systems. Finally, Section VII and Section VIII respectively conclude this survey and provide suggestions for the future exploration.

- Supervised Fine-Tuning (SFT). Different from the pre-training process which requires a huge demand for computational resources, SFT usually trains the model on a smaller scale but well-designed high-quality instances to unlock LLMs' ability to deal with prompts of multiple downstream tasks [46].

**c27ee0fb7a2760dc**
I. INTRODUCTION
Recently, the prevalent sampling strategies including top-k sampling [27] and nucleus sampling (i.e., top-p sampling) [28], have been widely used to sample vt from V based on the probability distribution p (v|v<t).

To achieve the goal, we propose a module-oriented taxonomy that classify the risks and their mitigation strategies associated with each module of an LLM system. For a specific risk, the module-oriented taxonomy can assist in quickly pinpointing modules necessitating attention, thereby helping engineers and developers to determine effective mitigation strategies. As illustrated in Figure 1, we provide an example of privacy leakage within an LLM system. Using our module-oriented taxonomy, we can attribute the privacy leakage issue to the input module, the language model module, and the toolchain module. Consequently, developers can fortify against adversarial prompts, employ privacy training, and rectify vulnerabilities in tools to mitigate the risk of privacy leakage.

Besides summarizing the potential risks of LLM systems and their mitigation methods, this paper also reviews widely-adopted risk assessment benchmarks and discusses the safety and security of prevalent LLM systems.

Large language models (LLMs) are the LMs that have billions or even more model parameters pre-trained on massive data, such as LLaMA [3], [4] and GPT families (e.g., GPT-3 [1], GPT-3.5 [29], and GPT-4 [30]). Recently, researchers discovered the scaling law [31], i.e., increasing the sizes of pre-training data and model parameters can significantly enhance an LM's capacity for downstream tasks. Such an "emerging ability" is a crucial distinction among the current LLMs and earlier small-scale LMs.

Network Architecture. Among existing LLMs, the mainstream network architecture is Transformer [32], which is a well-known neural network structure in Natural Language Processing (NLP). In general, an LLM is stacked by several Transformer blocks, and each block consists of a multi-head attention layer as well as a feed-forward layer. Additionally, trainable matrices enable mappings between the vocabulary space and the representation space. The key of Transformer is using attention mechanism [32] to reflect the correlations between tokens via attention scores. Therefore, the attention layers could capture the semantically meaningful interactions among different tokens to facilitate representation learning.

To sum up, this paper makes the following contributions.
- We conduct a comprehensive survey of risks and mitigation methods associated with each module of an LLM system, as well as review the benchmarks for evaluating the safety and security of LLM systems.

 ### Analysis ###"""

data = {
    "n_predict": 1000,             # Predictions slider (max tokens)
    "temperature": 0.25,            # Temperature slider
    "repeat_penalty": 1.0,         # Penalize repeat sequence slider
    "repeat_last_n": 256,          # Consider N last tokens for penalize slider
    "top_k": 40,                   # Top-K sampling slider
    "top_p": 0.95,                 # Top-P sampling slider
    "min_p": 0.05,                 # Min-P sampling slider
    "tfs_z": 1,                    # Tail-free sampling parameter, reduces the impact of low-probability tokens
    "typical_p": 1,                # Controls how "typical" the sampling should be (1 means standard sampling)
    "presence_penalty": 0.2,         #  penalty for tokens that have appeared at all
    "frequency_penalty": 0.2,        # penalty based on how frequently tokens have appeared
    "mirostat": 0,                 # "no Mirostat" radio option
    "mirostat_tau": 5,            # Mirostat target complexity (only if mirostat enabled)
    "mirostat_eta": 0.1,          # Mirostat learning rate (only if mirostat enabled)
    "n_probs": 0,                 # Show Probabilities slider
    "min_keep": 0,                # Mkeep minimum number of candidates per sampling
    "stop": ["#END#"],
    "stream": True,
    "prompt": content,
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
        stream=True
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
                            print(content, end='', flush=True)
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
    