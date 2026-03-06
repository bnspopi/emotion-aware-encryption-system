def detect_emotion(text):
    text = text.lower()

    emotions = {
        "anger": ["hate", "angry", "mad", "furious"],
        "joy": ["love", "happy", "great", "amazing"],
        "sadness": ["sad", "cry", "depressed", "upset"],
        "fear": ["scared", "afraid", "fear", "terrified"],
        "surprise": ["wow", "surprised", "unexpected"]
    }

    scores = {}

    for emotion, words in emotions.items():
        scores[emotion] = sum(word in text for word in words)

    detected = max(scores, key=scores.get)

    total = sum(scores.values()) + 1
    confidence = round((scores[detected] / total) * 100, 2)

    return {
        "emotion": detected,
        "confidence": confidence,
        "scores": scores
    }
