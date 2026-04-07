import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "knowledge_base.json")

def load_knowledge_base():
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print("Error loading knowledge base:", e)
        return []

def get_all_texts(knowledge_base):
    return [item["text"] for item in knowledge_base if "text" in item]
     