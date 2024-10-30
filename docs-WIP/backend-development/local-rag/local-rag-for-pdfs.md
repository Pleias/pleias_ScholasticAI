# Local RAG for PDFs

## Frameworks

The 3 most common RAG frameworks are LangChain, Haystack and LlamaIndex. They all support .pdf input natively ([LC](https://medium.com/@drjulija/how-i-built-a-basic-rag-for-pdf-qa-in-a-few-lines-of-python-code-9849c32e59f0), [HS](https://haystack.deepset.ai/tutorials/30\_file\_type\_preprocessing\_index\_pipeline), [LI](https://www.llamaindex.ai/blog/introducing-llamacloud-and-llamaparse-af8cedf9006b))

Here is a quick recap of their differences:



<table data-header-hidden><thead><tr><th></th><th width="78"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Framework</strong></td><td><strong>Fully Local</strong></td><td><strong>Best for</strong></td><td><strong>Advantages</strong></td><td><strong>Disadvantages</strong></td></tr><tr><td>LangChain</td><td>Yes</td><td>Modular, custom RAG workflows</td><td>Highly flexible, wide integration, strong community</td><td>Complexity, can be resource-intensive</td></tr><tr><td>Haystack</td><td>Yes</td><td>Robust PDF and document RAG</td><td>Optimized pipelines, strong document store support</td><td>Less modular, steeper learning curve</td></tr><tr><td>LlamaIndex</td><td>Yes</td><td>Large document collections</td><td>Efficient index-based retrieval, low-latency</td><td>Limited flexibility in complex workflows</td></tr></tbody></table>

## Integration with llamafiles and llama.cpp

All three frameworks seem to integrate quite smoothly with llamafiles and llama.cpp (clink on the links for the detailed doc)

|             | LangChain                                                                                                                                                                          | Haystack                                                                         | LlamaIndex                                                                       |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Llamafiles  | ✅ ([🔗](https://python.langchain.com/v0.1/docs/guides/development/local\_llms/),[🔗](https://python.langchain.com/v0.1/docs/use\_cases/question\_answering/local\_retrieval\_qa/)) | ✅ ([🔗](https://haystack.deepset.ai/integrations/llamafile)) through open-ai API | ✅ ([🔗](https://docs.llamaindex.ai/en/stable/examples/llm/llamafile/))           |
| llama.cpp   | ✅([🔗](https://python.langchain.com/docs/integrations/llms/llamacpp/))                                                                                                             |  ✅([🔗](https://haystack.deepset.ai/integrations/llama\_cpp))                    | ✅([🔗](https://docs.llamaindex.ai/en/stable/examples/llm/llama\_2\_llama\_cpp/)) |

At first sight, LangChain's integration with llamafiles and llama.cpp seems to be the most sophisticated and modular. To be tried.





