---
description: >-
  The goal is to study llamafiles inference speed and compare it to mlx
  inference speed in order to decide which framework is better to use for
  application.
icon: file-mov
---

# Llama files compared with MLX inference

## Model descriptions&#x20;

We have chosen the following models for our analysis. To measure the speed we run the inference and generation steps (up to 125 steps) for each models with a prompts of 3 different length. The first prompt was a short one - just 5 tokens, the second one was approximately 1200 tokens and the last one was around 4K tokens.

1. Llama-3.2-1B-Instruct - fp16 quantization
2. Llama-3.2-3B-Instruct  - fp16 quantization
3. Meta-Llama-3-8B-Instruct  - 2 bits quantization
4. Meta-Llama-3-8B-Instruct  - 4 bits quantization
5. Meta-Llama-3-8B-Instruct  - 8 bits quantization

Moreover, we also converted Marianne models to both formats to check the speed.



{% embed url="https://docs.google.com/spreadsheets/d/1N3j9OOkx4viuK-2L6JUVF6Ofc9jZJjJKbjDfrU54NHE/edit?usp=sharing" fullWidth="true" %}

Some interesting observations:

1. Llama 1B work slower than all models, probably because small models are not optimized in this frameworks.&#x20;
2. The results for Long  prompts \~ 1250 tokens and very long prompt \~ 3K tokens are almost the same, because of truncation under the hood. Probably will need to check if we can control it, but I haven't find it quickly&#x20;
3. Results for 3B looks weird if compare long prompt to very long prompt.





## Usage exemples

### MLX&#x20;

To convert any llm to mlx format run the following command. They also support architectures for Bert/Roberta etc. Bassicly converting a model means just to resave tensor into numpy npz format, and then load it into mlx rewritten architecture, where nn.Modules is still used, but all torch tensors replaced with mx tensors format. So, overall I think the design of this library is quite friendly for PyTorch users.&#x20;

```bash
python -m mlx_lm.convert \
    --hf-path PleIAs/llama-reasoning-rag \
    --mlx-path llama-reasoning-rag-mlx-4bits \
    -q\
    --q-bits 4\
    --upload-repo PleIAs/llama-reasoning-rag-converted
```

To use the model:&#x20;

```python
from mlx_lm import load, generate
model, tokenizer = load(path_or_hf_repo ='llama-reasoning-rag-mlx-4bits')
response = generate(model, tokenizer, prompt="Hello, tell me joke", verbose=True)
```

### Llamafiles

To run llamafiles we need to make to steps:

1. download the last release of  llamafiles server: [https://github.com/Mozilla-Ocho/llamafile/releases](https://github.com/Mozilla-Ocho/llamafile/releases)
2. convert model to gguf format: [https://github.com/ggerganov/llama.cpp/discussions/7927](https://github.com/ggerganov/llama.cpp/discussions/7927)
3.  run in terminal&#x20;

    ```bash
    llamafile-0.8.13 ./bin/llamafile --server -m path_to_gguf_model
    ```

#### converting to gguf format&#x20;

1. we need to pay attention to pre tokenization, as llamafiles supports some limited tokenization pipeline in terms of regex etc due to c++ restrictions&#x20;
2. to convert to gguf, you first need to run update file, please see tutorial for more details. Some models might not work, so so workaround is just to delete this models from list of models where you insert your new model.&#x20;
3. after model is converted llama.cpp might through an error such as unkown pre tokneization = your model name, in this case you can just comment all lines in the convert sript which writes to this gguf.writer.pretokenizer.&#x20;

Overall, the product is still on the development stage so the code changes quite quickly, so I would say it quite difficult to develop in top of it due to luck of documentation, rapid changes, and C++ code base which restrict our ability to adapt code for our purposes. For RAG I would advice to use integration into other libraries such as LLama Index and hope that their developers will trouble shoot all versions.&#x20;

## Speed measurements of converted models&#x20;

Using the recipes provided in the previous sections I converted two models. One into mlx format and second into llamafile format. Both model has been published on HF.&#x20;

{% embed url="https://huggingface.co/aapoliakova/reasoning-rag-mlx/upload/main" %}

{% embed url="https://huggingface.co/aapoliakova/marianne_300m_2048_20000/tree/main" %}

We also made some experiments to measure inference speed:&#x20;

{% embed url="https://docs.google.com/spreadsheets/d/1N3j9OOkx4viuK-2L6JUVF6Ofc9jZJjJKbjDfrU54NHE/edit?usp=sharing" %}

## Running on Windows&#x20;

On Windows, our aim has been twofold:

* Assess the viability of a full-CPU inference
* Compare the llamafiles framework with llama.cpp, both in terms of inference speed and ease of use

Device specifications:

* Windows 64x
* 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz 2.80 GHz
* RAM: 32.0 Go

### 1. CPU viability

We have not me any blocking limit on running LLM inference with the current device. However, the model inference tends to become relatively slow when running bigger models and lower quantizations.

Our main test framework relied on llama.cpp through the llama-cpp-python library. The prompt we used is displayed at the end, it enables to have 1000+ tokens in the prompt and generation, and thus a solid basis to average upon.

Interestingly, we do not observe real changes of magnitude regarding the generation speed, whereas prompt reading speed plummets with the model size.

Unfortunately, we were not able to conduct the same test on llamafiles due to the 4Go execution limit on Windows.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

## 2. Llamafiles vs llama.cpp comparison

#### A. Performance

On our benchmark and for the models we were able to try, llamafiles overperforms llama.cpp by c. +30% inference speed on average.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### B. Ease of use

Although llamafiles promises a seamless, integrated experience of running LLMs locally, we were not fully convinced by this experience. This is due to:

* Inconsistencies in the API depending on when models when generated. We used 2 main sources for our llamafiles: Mozilla's HF models ([for instance](https://huggingface.co/Mozilla/Meta-Llama-3-8B-Instruct-llamafile/tree/main)) and another source ([for instance](https://huggingface.co/wirthual/Meta-Llama-3.2-1B-Instruct-llamafile/blob/main/Meta-Llama-3.2-1B-Instruct-Q8\_0.llamafile)). The commands to run models and were different in both cases, which took us significant time to solve. \
  In the first case, when we wanted to run prompts without opening a browser window, we had to run `./Llama-3.2-1B-Instruct.F16.llamafile --cli -p 'Tell me a joke'` while in the second case we had to run`Llama-3.2-1B-Instruct.F16.llamafile -p 'Tell me a joke'`. While this may seem a minor difference, we did not understand these discrepancies and they led us to lose significant time: the second command appears to freeze the model when applied to the first one.
* Size limit for windows: Windows apparently prevents to execute files above 4Go, which concerns most 16b models. On the other hand, llama.cpp does not have this limit
* Inconsistencies across devices and environments: some models worked for MacOs and not Windows, for instance [this one](https://huggingface.co/wirthual/Meta-Llama-3.2-1B-Instruct-llamafile/blob/main/Meta-Llama-3.2-1B-Instruct-Q4\_K\_M.llamafile)

On the other hand, llama.cpp:

* Enables a user friendly interface through the llama-cpp-python library, which allows to call llama-cpp in python rather than from the terminal
* Allows to use any model without distinction of size, and without having to download them separately as a HF link is enough to call the model

For these reasons, we found llama.cpp easier to use.



## Appendix

Main prompt used for Windows benchmarking ("long prompt")

```
The Future of Sustainable Cities and Human Life

The world is currently at a pivotal moment when it comes to environmental sustainability and the future of human settlements. As global populations continue to rise and the effects of climate change intensify, cities must adapt to survive and thrive. Imagine you're an urban planner tasked with creating a city that will be both livable and sustainable in the year 2100. This city needs to accommodate a population of 10 million people while minimizing its environmental footprint and providing a high quality of life for all its residents.

Design the basic structure of the city:

What are the primary environmental challenges you would consider in designing the city? Think about rising sea levels, increased frequency of extreme weather events, and shrinking natural resources.
How would you design public transportation to reduce carbon emissions? Consider how advances in technology, such as autonomous electric vehicles, high-speed rail, and even aerial transport systems like drones, might play a role.
What materials would you use in constructing buildings? Could you incorporate renewable materials or design modular buildings that can be easily repurposed or recycled?
How would you incorporate green spaces and biodiversity into the city design? Could parks, urban forests, or vertical gardens play a role in improving air quality and providing recreational areas for the population?
Economic and Social Considerations:

How would you ensure that the city is affordable and accessible to people of different income levels? Could you design housing that is both eco-friendly and affordable for lower-income residents?
In a future where automation and AI play a significant role in the economy, how would you create jobs for the residents of your city? What industries might flourish in this new economy, and how can the city support them?
How would you handle the distribution of resources like water, energy, and food? Could your city rely entirely on renewable energy sources such as solar, wind, or geothermal power? How would you manage waste, particularly in a city of 10 million people?
Could your city become a hub for education and innovation? How would schools, universities, and research centers contribute to the city's sustainability and technological progress?
Governance and Policy:

How would you govern this city to ensure it remains sustainable for decades to come? What policies would you implement to maintain environmental protections, human rights, and economic fairness?
How would you involve citizens in decision-making processes? Could technology such as blockchain or digital voting systems increase transparency and participation in governance?
In the year 2100, what role do you think national governments will play in relation to city-states? Could your city operate independently or in collaboration with other cities around the world?
Technological Innovations:

Imagine the technology of the future. How could innovations in AI, biotechnology, and nanotechnology shape the everyday lives of the city's residents? Could AI-driven infrastructure anticipate the needs of the population, such as optimizing energy use or predicting the demand for certain services?
How would healthcare be delivered in this future city? Could telemedicine, robotics, and advanced medical treatments extend life expectancy or improve the overall health of the population? How might people access these services?
Could food production be integrated into the city itself? Vertical farms, lab-grown meats, and urban agriculture could reduce the need for importing food. How might you design these systems, and how could they contribute to the city's circular economy?
Cultural and Ethical Dimensions:

How would culture evolve in this highly technological and eco-conscious future city? Could art, music, and storytelling still thrive in a society focused on sustainability and innovation?
How would you ensure that the city remains inclusive and respects diversity? What would you do to make sure that people from various cultural, ethnic, and socioeconomic backgrounds feel welcome and have equal opportunities?
Could your city become a center for global cooperation on climate change and other pressing challenges? How might the residents engage with the wider world, perhaps serving as ambassadors for new ways of living in harmony with the planet?
Exploring the Future: Imagine living in this city yourself. Describe a day in the life of a resident:

What does your home look like? Is it an apartment in a high-tech skyscraper or a small house in a suburban community?
How do you travel around the city? Do you walk, bike, use an autonomous vehicle, or perhaps take a high-speed underground transit system?
Where do you work, and what is your job? Are you involved in the city's governance, work in a tech startup, or perhaps contribute to scientific research that advances human knowledge?
What do you do for leisure? Do you spend time in a park, visit a cultural center, or maybe enjoy virtual reality experiences that transport you to other parts of the world or even other planets?
How do you interact with other people? Are social networks and virtual reality the primary forms of communication, or do face-to-face interactions still play a central role in building community?
Challenges and Trade-offs:

What are the potential downsides to living in this future city? Could increased reliance on technology lead to issues of privacy or loss of personal autonomy? How might you address these concerns?
How would you balance the need for economic growth with the importance of protecting the environment? Could your city become a model for "degrowth" – an economic strategy that prioritizes sustainability over continuous expansion?
As technology and automation take on more tasks, how would you ensure that the human element remains essential in your city's culture? Could arts, education, and personal development become more valued than economic productivity?
Speculative Future Scenarios:

Imagine your city in the face of unexpected global events, such as a sudden climate disaster, a pandemic, or geopolitical conflict. How would the city adapt to these challenges? Could it offer solutions or become a refuge for others affected by such crises?
How might advancements in space exploration or colonization affect the design of your city? Could space travel become common, with some residents commuting to other planets or space stations? How would you prepare the city for a future where Earth might no longer be the only home for humanity?

```













