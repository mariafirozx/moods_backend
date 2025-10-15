# from functools import lru_cache

##my original -->>

# @lru_cache(maxsize=1)
# def model():
#     from transformers import pipeline
#     return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", framework="tf", return_all_scores=True)

# def text_classify(text: str):
#     classifier = model();
#     res = classifier(text)
    
#     return res




##using lazy load method -->>

# from transformers import pipeline

# _classifier = None

# def text_classify(text: str):
#     global _classifier
#     if _classifier is None:
#        _classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True, low_cpu_mem_usage=True)
#     res = _classifier(text)
       

#     return res


##using hugging face API interference

#hugging face API token -> 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

import os;
import requests;

API_URL = "https://router.huggingface.co/hf-inference/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"} 

def text_classify(text:str):
    res = requests.post(API_URL, headers=headers, json={"inputs": text})

    return res.json()
