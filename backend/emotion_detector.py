from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def detect_emotion(text):

    results = emotion_model(text)[0]

    scores = {}

    for r in results:
        scores[r["label"]] = round(r["score"] * 100, 2)

    # sort emotions by score
    sorted_emotions = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # top 2 emotions
    top1 = sorted_emotions[0]
    top2 = sorted_emotions[1]

    emotion_text = f"{top1[0]} + {top2[0]}"
    confidence_text = f"{top1[1]}% + {top2[1]}%"

    return {
        "emotion": emotion_text,
        "confidence": confidence_text,
        "scores": scores
    }
