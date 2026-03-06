def detect_emotion(text):

    emotions = {
        "joy": ["happy", "great", "love", "excited", "awesome"],
        "sadness": ["sad", "cry", "depressed", "unhappy"],
        "anger": ["hate", "angry", "mad", "furious"],
        "fear": ["scared", "fear", "afraid", "worried"]
    }

    text = text.lower()

    for emotion, words in emotions.items():
        for word in words:
            if word in text:
                return emotion

    return "neutral"
