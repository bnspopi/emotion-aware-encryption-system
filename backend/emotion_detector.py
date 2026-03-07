from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

def detect_emotion(text):

    results = emotion_model(text)[0]

    emotions = []

    for r in results:
        label = r["label"]
        score = round(r["score"] * 100, 2)

        # Ignore neutral
        if label != "neutral":
            emotions.append((label, score))

    emotions = sorted(emotions, key=lambda x: x[1], reverse=True)

    top1 = emotions[0]
    top2 = emotions[1]

    emotion_text = f"{top1[0]} + {top2[0]}"
    confidence_text = f"{top1[1]}% + {top2[1]}%"

    return {
        "emotion": emotion_text,
        "confidence": confidence_text
    }
