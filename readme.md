# ScholasticAI

<img src="static/ScholasticAI_Pleias_logo.png" alt="ScholasticAI Pleias logo" width="700">


**ScholasticAI** is a versatile desktop tool designed for **retrieval-augmented generation (RAG**. It allows you to upload and analyze local PDFs, retrieve information using conversational AI, and verify answers with references grounded in your own documents, as well as querying external databases. While we built this application mainly for research articles, you can use it for other purposes.

The app was made under the philosphy of **complete local deployement**, running efficiently on consumer grade **GPU-less** laptops or desktops. In order to achieve that, we rely on **Pleias's own AI foundation models**, which are **SoTA small models for RAG**, **European AI Act compliant** and most importantly **completely open** (weights, corpus and code). 

**ScholasticAI** can run in systems having at least these specs:

- OS : Windows - MacOS
- Ryzen 5 3000 series processor , Intel Core i5 series (8th gen), Apple M1 Processor
- 8GB of Ram

<img src="static/mozilla_logo.png" alt="Mozilla logo" width="150">

We are very grateful to the **Mozilla foundation** (Local AI builders program), who supported the development of this application.

### Table of Contents

1. [How to Use the App](#1-how-to-use-the-app)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Download and Load the Model](#step-2-download-and-load-the-model)
    - [Step 3: Install Dependencies](#step-3-install-dependencies)
    - [Step 4: Run the Application](#step-4-run-the-application)
2. [Working with the App](#2-working-with-the-app)
3. [Model](#3-model)
    - [Description](#description)
    - [Training](#training)
4. [Remarks](#4-remarks)
    - [First time use](#first-time-use)
    - [Bright mode](#bright-mode)
    - [CPU usage](#cpu-usage)
5. [Attribution](#5-attribution)


---

## 1. How to Use the App

### Step 1: Clone the Repository
```bash
git clone https://github.com/Pleias/pleias_ScholasticAI
cd pleias_ScholasticAI
```

### Step 2: Download and Load the Model
1. Download the **llamafile executable** (v0.8.13):
   ```bash
   wget https://github.com/Mozilla-Ocho/llamafile/releases/download/0.8.13/llamafile-0.8.13
   chmod +x llamafile-0.8.13
   ```
2. Download the **PleIAs-360m model**:
   - [Model Link](https://huggingface.co/PleIAs/Pleias-360m-RAG)
   - [GGUF version] (https://huggingface.co/PleIAs/pleias360_gguf)

3. Load the model locally:
   ```bash
   ./llamafile-0.8.13 -m pleias360_bf16.gguf -c 2048 # adapt with your local paths
   ```
   - This will expose an API at `http://127.0.0.1:8080`.


> Note: our implementation relies on [llamafiles](https://github.com/Mozilla-Ocho/llamafile) and Pleias's models. You can find the full list of available PLeias models [here](https://huggingface.co/collections/PleIAs/common-models-674cd0667951ab7c4ef84cc4). Alternatively, you can use any llamafile or model in the .gguf format with the code above

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python -m src.main
```
**Important** Due to the specialized nature of the training applied to our model, we suggest to always generate answers using a temperature of 0 (default parameter), in order to get results of the best quality. 

---

## 2. Working with the App

[![Watch the demo video](static/ScholasticAI_Pleias_video.png)](https://drive.google.com/file/d/1SpkTgavgOls3yITKPOPGqRmYL8u6tMm_/view?usp=sharing)

---


## 3. Model
**Pleias-360m-RAG 0.1** is a specialized language model designed by PleIAs for Retrieval-Augmented Generation.

Similarly to its base model, Pleias-360m, Pleias-360m-RAG 0.1 aims to be a fully open model (weights, code, data), only trained on content with a permissible license and fully compliant with the European AI Act.

### Description
PleIAs-360m-RAG is continuous pretraining of Pleias-360m on a new dataset of 45,088,768,000 tokens modeling common retrieval tasks. All the content of the dataset is ultimately coming from Common Corpus.

Pleias-360m-RAG includes the main features of the original base model:
* Only trained on open data under a permissible license and in compliance with the European AI Act. By design, all Pleias model are unable to output copyrighted content.
* Extensive multilingual support for main European languages: English, French, German, Spanish, Italian, Dutch, Latin, Portuguese and Polish.
* Extremely low level of toxicity and problematic content.

Pleias-360m-RAG supports retrieval-augmented generation with enhanced verifiability, source analysis and grounding on submitted sources. This includes:
* Standardized structure and special tokens to include queries, sources, references.
* Anticipation of various query forms in multiple languages, from actual drafted questions to unstructured list of keyword search.
* Source analysis/criticism which also acts as an integrated reranker step.
* Generation of ground answers with references and excerpts linked to the original sources.

Given its small size, Pleias-360m-RAG 0.1 was originally conceived as an experimental model. 

Initial tests have shown that the RAG design has significantly improved the factuality and verifiability of the model. Even when the grounding does not work perfectly, the information remains much closer to the original sources.

### Training
PleIAs-360m-RAG was trained at Jean-Zay with 16 h100s with Nanotron, the pretraining library from HuggingFace. 

PleIAs-360m-RAG derives from the last checkpoint of PleIAs-360m (518,000). The training schedule reused the last learning rate value (6e-5) without decay for 90,000 steps.

Training covers the entire RAG dataset we have been designing out of Common Corpus for 1 epoch.

Further experiments were made with different learning rate values: none of theses tests have provided a better convergence than the one obtained with the final learning rate from the base model.

As a specialized language model, PleIAs-360m-RAG will be unable to work properly with prompts that detracts from that design.


---

## 4. Remarks
### First time use
- If you launch the app for the first time, the BGE-M3 model for embedding will be downloaded. This should not take more than a few minutes depending on your internet connection. 
- Once initialized, you can:
  - Upload PDFs to the app.
  - Ask questions in the chat window.
  - Load additional documents at any time.

### Bright mode
- Pleias RAG app was designed for the bright mode for the moment. We strongly recommend you switch your laptop to bright mode before launching the app.


### CPU Usage
This application is optimized to run on CPU-only for local use. Running multiple other applications simultaneously may slow it down.

---


## 5. Attribution

This app leverages open-source tools and models, including:
- **PleIAs-360m-RAG**: A retrieval-augmented generation language model designed by Pleias.
- **llamafile**: Model loader and API server for efficient local inference.

All models and tools are designed to comply with the **European AI Act** and respect open licensing standards.
