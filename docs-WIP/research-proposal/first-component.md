---
description: description of how we can probably improve retrieval component.
---

# first component

Retrieval part could be described in 3 main steps. First step is the extraction step, where we can extract information from documents as well as it's metadata, utilize special extraction approach for tables etc. The second step is storing data for retrieval. Retrieval depends on chunking strategy and query.  There are a lot of techniques on how we can enhance user query, as well as a lot of chunking strategies which worth to try. And the last step is actually retrieval. Out current approach works quite slowly, so we could change it to bm25. On top of it, we could dig into rerankers or rank fusion approaches, which I would describe later.&#x20;

**Extraction step**

We need to find optimal extraction strategy for our pipeline. As we want to build system on top of BM25 search we must make a good work on information extraction step.&#x20;

My first suggestion is to extract metadata for each document and for each chunk. For example, for each paper we could extract keywords or abstract as a metadata, as well as for each chunk we could extract section name. This metadata could be utilized in different ways. First we could augment this chunks with this metadata: adding keywords might be helpful in case of BM2 search, second we can down out search by prefeltering papers by metadata and that use embedding search for example only on small subset.&#x20;

<table><thead><tr><th width="199">Extraction approach </th><th>Links/desciprion</th><th>Comments</th></tr></thead><tbody><tr><td>Docling</td><td><a href="https://ds4sd.github.io/docling/">https://ds4sd.github.io/docling/</a></td><td></td></tr><tr><td>Unstructured </td><td><a href="https://unstructured.io/">https://unstructured.io/</a></td><td></td></tr><tr><td>Yolo8</td><td></td><td></td></tr></tbody></table>

Second, I will suggest us to find more interesting approach to table extraction. For example augment each table row with column name and table description for more efficient search.&#x20;

Third, to improve our current approach we need to make our pipeline more robust. Before processing any doc, check if it corrupted or not, etc. Just, some security checks before we even start running anything at all. (this is for the app).&#x20;



**Chunking strategies**

We need to decide on chunks size, but the intuition behind it is the next: larger chunk size are save as it less chances to lose context information, but it also might lead to hallucination and lost in the middle problem.  So, we need to choose the optimal size for our models. Beside keyword augmentation, which I described earlier, we can also test some other techniques:&#x20;

| Chunking approach  | Links/description | Comments |
| ------------------ | ----------------- | -------- |
| Late chunking      |                   |          |
| 1B context on CPU  |                   |          |
|                    |                   |          |

**User query enhancement**

This part could be done only with additional LLM, so I don't think it's possible without speed lost, but there are also some interesting techniques which helps to align user language with the stored chunks for more effective search. Such as query translation, splitting complicated query into subqueries, abstract queries. We could consider some option in the future. Do we actually support multilingual queries, if so we could also store metadata for queries such as language. Also, if we want to utilize conversation history is a question. But we can enhance user query based on previous conversation.&#x20;

**Retrieval**

There are papers that shows that relevant chunks position affects the response generation quality. The goal is to position relevant chunks at the beginning or at the and of a prompt. Please see [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172) - Lost in the middle paper. To create such prompts we need to utilize reranker. Reranker is a model which takes in query and context and returns relevancy score. Usually people train something small Bert Like model, but if we don't want to train we could utilize reranker from cohere. We should keep in mind that this is quite expensive operation, so we need first extract for ex 5 the most relevant chunks using bm25 or semantic searach and do rerank on top of it.&#x20;

Hybrid search. We can also do bm25 + keyword + semantic and do rank fusion. Rank fusion is approach to combine rank of each chunk across sources via average score, or weighted sum etc.&#x20;

What we have missed at the first implementation that we actually must test all frameworks and approaches (keyword vs bm25 vs semantic) as intuition about the speed might be wrong for some dataset / implementation. So, it easily could be the case where semantic works faster than BM25 etc.&#x20;

Also, there are quite effective technique such as IRCot. It's Chain of thought retrieval in multiple steps. [https://arxiv.org/pdf/2212.10509](https://arxiv.org/pdf/2212.10509)

What I didn't have enough time to read about is knowledge graphs [https://arxiv.org/pdf/2409.13731](https://arxiv.org/pdf/2409.13731)









