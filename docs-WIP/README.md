---
description: Here is some ideas on how we can proceed with application
---

# Research proposal

Evaluation&#x20;

The most important thing in making improvements is good logging strategy and evaluation. To make evaluation of RAG system we need to evaluate all components. Out current system has two main components. The first one is retrieval component and second one is generation component. For each of this steps we need to create gold standard dataset manually.&#x20;

For **retrieval component** evaluation we would need to create ground truth context for each query. Given the retrieved context and ground truth context we can compute different metrics to measure quality of different retrival strategies. I would provide metrics description in a separate document, but for now it worth to mention that there are two main focus in evaluation:&#x20;

1. ranking based metrics - How high was the first relevant document ranked?
2. accuracy based metrics - Out of the documents we retrieved, how many were actually relevant?

For our use case the first class of metrics might be very interesting as the position of relevant chunk could affect the response results significantly. That is a hypothesis, so could be checked.&#x20;

The goal of this evaluation step is to determine optimal document extraction strategies, metadata augmentation strategy, effectiveness of using embeddings, bm25, rank fusion or other retrieval techniques, which I will also describe in a different document.&#x20;

To conclude, creating ground truth references will allow us to measure the effectiveness of out retrieval approach, give us a quantative understanding of the results in terms of accuracy, speed etc.&#x20;

For **generation component** we need to evaluate different models given the assumption that chunks are ground truth. I suggest to make this evaluation using a question based approach. First we could evaluate each response by asking focus group (which I think going to be out team) several questions:

1. Does response fully answers user question?&#x20;
2. Is response is consistent with information from retrieved chunks
3. Rate the quality of the response&#x20;

And many others. This step is important for choosing the best model for response generation fiven the context length, inference speed and all other factors.&#x20;



This research stage and app development requires us to adapt our code base. For the research stage saving each step of the pipeline is crucial, as we need properly log our experiments to analyse the results, whereas for application this approach just produce extra artifacts. So, at the reaserch stage we need to adapt the code base. In the future, when we come up with the best decision for each component, for the application we could restructure our code base, so that it might be easily integrated with another ui (React or whateever). My suggestion, would be split pipeline into 2 main end points. First endpoint is for document loading and building the document store. This step might be slower than the second one.  Second is a runtime endpoint - where user actually makes queries and retrieves the answer.&#x20;



