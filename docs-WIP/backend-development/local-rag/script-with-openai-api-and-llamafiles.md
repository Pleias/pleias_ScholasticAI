# Script with openai api and llamafiles

```python
#!/usr/bin/env python3
from openai import OpenAI
client = OpenAI( 
    base_url = "http://localhost:8080/v1", # base_url="http://localhost:8080/v1",
    api_key = "sk-no-key-required"
)
completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=[
        {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
        {"role": "user", "content": "Write a limerick about python exceptions"}
    ]
)
print(completion.choices[0].message)
```

