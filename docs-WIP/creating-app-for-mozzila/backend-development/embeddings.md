# Embeddings

Ongoing tests/benchmark for local efficient embeddings.

For now simplest thing would be to use lancedb but not sure it will be well supported for local inference.



## Hybrid search&#x20;

We want to test existing solution with hybrid search, for the first test I will compare 2 solution on one dataset this is waviate with hybrid search and lancedb with hybrid search. We want to test this all locally on macos cpu. Right now for simplic

The 2 main interests are:

How fast we can we build index for out dataset?&#x20;

How fast we can retrive top 3 answers?&#x20;



Maybe we need to take a look at hystack as well because as I remember it also supports hybrid search.  I know that hystack is less user friendly than the other libs but highly controllable and might support additional functionality&#x20;

To run this experiments I used the next tutorials

for lancdb&#x20;

{% embed url="https://github.com/lancedb/vectordb-recipes/tree/main/examples/Youtube-Search-QA-Bot" %}

{% embed url="https://haystack.deepset.ai/tutorials/26_hybrid_retrieval" %}

{% embed url="https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/" %}

## Weaviate

Requires one more docker or client running on the background , installation is time consuming, so prefer to switch more lightweight solutions&#x20;

## Lancdb&#x20;

This is minimalistic examples with lancb vector storage and hybrid search, so for query from the code and sentence transformers and rotten-tomatos index , one hybrid search took 27 ms. Which is fine.&#x20;

```python
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector

model = get_registry().get("sentence-transformers").create(name="all-MiniLM-L6-v2", device="cpu")

from datasets import load_dataset
ds_builder = load_dataset("rotten_tomatoes", split='train')
ds_builder = ds_builder.to_pandas()

class VanillaDocuments(LanceModel):
    vector: Vector(model.ndims()) = model.VectorField()  # Default field
    text: str = (model.SourceField())  # the Columns (field) in DB whose Embedding we'll create
    
import lancedb

db = lancedb.connect("./db")
vanilla_table = db.create_table("vanilla_documents", schema=VanillaDocuments)

vanilla_table.add(ds_builder)  # ingest docs with auto-vectorization
vanilla_table.create_fts_index("text")  

QUERY = "implement corpus management with event handling"
vanilla_table.search(QUERY, query_type="hybrid").limit(3).to_pandas()
```

This is link to tutorial with llamaindex integration and colbert&#x20;

{% embed url="https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/" %}

### Lancdb with contextual retrival&#x20;



{% embed url="https://colab.research.google.com/github/lancedb/vectordb-recipes/blob/main/examples/Contextual-RAG/Anthropic_Contextual_RAG.ipynb#scrollTo=kQ9MggTd1nQU" %}

{% embed url="https://www.anthropic.com/news/contextual-retrieval" %}
