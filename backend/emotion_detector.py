from transformers import pipeline

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def detect_emotion(text):

    results = emotion_pipeline(text)[0]

    scores = {}

    for r in results:
        scores[r["label"]] = round(r["score"] * 100, 2)

    detected_emotion = max(scores, key=scores.get)
    confidence = scores[detected_emotion]

    return {
        "emotion": detected_emotion,
        "confidence": confidence,
        "scores": scores
    }
