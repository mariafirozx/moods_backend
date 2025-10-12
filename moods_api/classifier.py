from functools import lru_cache


@lru_cache(maxsize=1)
def model():
    from transformers import pipeline
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", framework="tf", return_all_scores=True)

def text_classify(text: str):
    # classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
    classifier = model();
    res = classifier(text)
    
    return res


