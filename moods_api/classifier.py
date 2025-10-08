from transformers import pipeline

def text_classify(text: str):
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

    res = classifier(text)
    
    return res


