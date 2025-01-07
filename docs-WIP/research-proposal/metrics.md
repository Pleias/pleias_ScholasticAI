---
description: metrics for evaluation
---

# metrics

**Information Retrieval (IR) Metrics:**

We can adapt traditional IR metrics commonly used in search engine evaluation to assess the performance of our RAG retrievers.

**Ranking-Based Metrics:** These metrics focus on the order in which relevant documents are retrieved:

* Hit Rate: Did we retrieve at least one relevant document?
* Mean Reciprocal Rank (MRR): How high was the first relevant document ranked?
* Normalized Discounted Cumulative Gain (NDCG): Considers both the relevance and the position of all retrieved documents.

**Predictive Quality Metrics:** These metrics measure the accuracy of the retriever in identifying relevant documents:

* Precision: Out of the documents we retrieved, how many were actually relevant?
* Recall: Out of all the relevant documents, how many did we retrieve?
* Mean Average Precision (MAP): The average precision across multiple queries.
* F1-Score: A balanced measure that combines precision and recall.

We can also create synthetic dataset for retrival evaluation and even use LLM as a judge.&#x20;

To create synthetic, we need to cluster similar chunks, sample from the group and generate queries that could be answered given only this information. That's how we can get ground truth context for each query.&#x20;

We can also use LLM as a judge - ask LLM to mark each chunk as 0 - not relevant to the query, 1 - somehow relevant, 2 relevant. But before we can you the judge on synthentic we still need to create manual dataset, as using LLMs requires prompt tuning, according to find the prompt which gives the most aligned labels to real data.&#x20;
