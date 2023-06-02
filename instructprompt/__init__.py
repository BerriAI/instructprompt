__version__ = '0.1.5'

import chromadb
import random


chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="user_instructprompt_collection")

def add(instruction: str): 
    id = random.randint(1, 9999)
    collection.add(
        documents=[instruction],
        ids=[str(id)]
    )
    print("✅ instruction added")
    return

def list(): 
    return collection.get()["documents"]

def query(query: str): 
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    instructions = ""
    for document in results["documents"][0]: 
        instructions += document + "\n"
    return instructions

