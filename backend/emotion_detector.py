from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text):
    scores = emotion_model(text)[0]

    scores = sorted(scores, key=lambda x: x["score"], reverse=True)

    top1 = scores[0]["label"]
    top2 = scores[1]["label"]

    return f"{top1} + {top2}"
