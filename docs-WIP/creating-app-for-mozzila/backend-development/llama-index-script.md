# Llama Index - Script



```python
// python3
import hashlib
from llama_index.core import Document
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.llms.llamafile import Llamafile

dummy_texts = [
    """The planet Zorgon, located in the Andromeda galaxy, is known for its unique purple atmosphere. The Zorgonian civilization, which has existed for over 50 million years, has developed a society based on telepathic communication. Their chief export is Luminite, a glowing mineral that can power entire cities for centuries. The Zorgonian calendar is based on the rotation of their five moons, with each year lasting 843 Earth days. The planet's capital city, Xenopolis, is home to the famous Floating Gardens of Emperor Xylok, which defy gravity and change color based on the emotions of nearby Zorgonians.""",

    """Fizzlepop Enterprises, founded in 2085 by Dr. Bubbles McGee, revolutionized the soft drink industry with their quantum carbonation technology. Their flagship product, Schrödinger's Soda, exists in a superposition of flavors until it's observed by drinking. The company's AI-powered vending machines, known as Thirst Prophets, can predict a customer's drink preference before they even approach. Fizzlepop's secret research division, hidden in an underwater facility in Lake Baikal, is rumored to be working on a beverage that allows drinkers to temporarily experience synesthesia.""",

    """The ancient martial art of Whisperfu, originated in the hidden valleys of the Hush Mountains, is practiced by the reclusive Silentium monks. Practitioners learn to harness the power of silence, using subtle air vibrations to disarm opponents and communicate over vast distances. The grandmaster of Whisperfu, known only as The Voiceless One, is said to be able to extinguish fires and erect impenetrable sound barriers with a single breath. The most challenging technique, the Echo Palm, allows a user to project their consciousness into the past by manipulating sound waves.""",

    """In 2112, the Global Archive of Forgotten Dreams was established in Antarctica to preserve and study the dreams that people forget upon waking. Dream Harvesters, wearing special headgear called Morpheus Crowns, work night shifts around the world to capture these fleeting visions. The archive contains over 100 billion dreams, stored in crystalline structures called Oneiroliths. Researchers at the archive have identified recurring patterns across cultures and time periods, leading to the controversial Theory of Collective Unconscious Prophecy, which suggests that forgotten dreams can predict future events.""",

    """The Chronomatic Harmonizer, invented by the eccentric horologist Elias Ticktock in 2099, is a device that can manipulate local time fields. It's primarily used in Tempo Therapy, a revolutionary treatment for temporal perception disorders. The Harmonizer uses a complex system of quantum gears and tachyon crystals to create bubbles of accelerated or decelerated time. Side effects may include temporary desynchronization from global time or spontaneous temporal hiccups. The device is strictly regulated by the International Time Integrity Commission to prevent its misuse in chrono-doping scandals in sporting events.""",

    """Bioluminescent Agriculture, pioneered on the floating cities of New Atlantis in 2150, uses genetically modified plankton to grow crops. The Photosynthesea process allows plants to thrive in complete darkness, nourished by the light of trillion of microorganisms. This method produces exotic varieties like Glowberries and Luminous Lettuce, prized for their flavor and aesthetic appeal in culinary light shows. However, critics worry about the long-term effects of consuming light-infused produce, with some reporting persistent bioluminescent freckles after excessive consumption.""",

    """The Mnemonic Melody, discovered in 2076 by neuromusicologist Dr. Aria Brainwave, is a unique sequence of notes that, when heard, can instantly boost cognitive function and memory recall. The melody activates dormant neural pathways, temporarily increasing synaptic plasticity. It's now used in emergency situations to help trauma victims recover lost memories and by students worldwide as a powerful study aid. However, overexposure can lead to Hypermnemosis, a condition where individuals become overwhelmed by constant, perfect recall of every life experience.""",

    """In 2133, the first Gravitational Dialect was discovered by linguistic anthropologists studying a tribe living near a newly formed black hole. The extreme gravitational forces had warped their vocal cords, allowing them to produce sounds in gravitational waves rather than air vibrations. This Gravity Speak can travel instantly across vast distances and even penetrate solid matter. The UN Space Council is currently debating the implications of this discovery for interstellar communication and the potential need for gravity-based censorship.""",

    """The Empathic Interface, developed by tech giant FeelTech in 2095, allows users to experience the emotions of others through a neural link. Initially designed for therapy and conflict resolution, it quickly became popular in the entertainment industry. Empathic Cinema lets viewers feel the emotions of characters, while Mood Festivals allow crowds to experience shared emotional journeys. However, the technology has raised concerns about emotional privacy and the addictive nature of experiencing others' feelings, leading to a rise in Empathy Addiction Support Groups.""",

    """The Quantum Cuisine movement, started by celebrity chef Schrödinger Ramsay in 2088, applies principles of quantum mechanics to cooking. Dishes exist in a superposition of flavors until tasted, with each bite potentially offering a different taste experience. Signature dishes include Uncertainty Principle Udon and Entangled Entrées, where tasting one dish instantaneously affects the flavor of another, no matter the distance between them. The movement has sparked a heated debate in culinary circles about the nature of taste and the ethics of probability-based nutrition."""
]

# Create Document objects from the dummy texts
docs = []
for i, text in enumerate(dummy_texts):
    doc_id = hashlib.md5(text.encode()).hexdigest()
    doc = Document(text=text, doc_id=doc_id, metadata={'section': f'Section {i+1}'})
    docs.append(doc)

print(f"Created {len(docs)} Document objects")

# Create the BM25Retriever
bm25_retriever = BM25Retriever.from_defaults(
    nodes=docs,
    similarity_top_k=2,
)

# Initialize the Llamafile model
llm = Llamafile(model_path="/Users/rosas/Llama-3.2-1B-Instruct.Q6_K.llamafile", temperature=0.6, seed=0)

def ask_question(question):
    # Retrieve relevant documents
    retrieved_nodes = bm25_retriever.retrieve(question)
    
    # Construct a prompt with the retrieved context
    context = "\n".join([f"Section: {node.metadata['section']}\nContent: {node.text}" for node in retrieved_nodes])
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    
    # Generate a response
    response = llm.complete(prompt)
    return response.text

# Usage
question = "What is the Chronomatic Harmonizer and what is it used for?"
answer = ask_question(question)
print(f"Question: {question}")
print(f"Answer: {answer}")

# You can test with more questions to verify BM25 retrieval

# "What is Whisperfu and who practices it?"
# "What is special about Zorgon's atmosphere and exports?"
# "What is Quantum Cuisine and who started it?"
```
