# from functools import lru_cache


# @lru_cache(maxsize=1)
# def model():
#     from transformers import pipeline
#     return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", framework="tf", return_all_scores=True)

# def text_classify(text: str):
#     # classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
#     classifier = model();
#     res = classifier(text)
    
#     return res


from transformers import pipeline

_classifier = None

def text_classify(text: str):
    global _classifier
    if _classifier is None:
       _classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True, low_cpu_mem_usage=True)
    res = _classifier(text)
       

    return res