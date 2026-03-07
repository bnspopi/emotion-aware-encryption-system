def detect_emotion(text):

    text = text.lower()

    joy_words = ["ecstatic","happy","excited","love","great","joy"]
    anxiety_words = ["anxious","nervous","deadline","stress"]
    anger_words = ["hate","angry","mad"]
    sadness_words = ["sad","depressed","cry"]

    scores = {
        "joy": sum(word in text for word in joy_words),
        "anxiety": sum(word in text for word in anxiety_words),
        "anger": sum(word in text for word in anger_words),
        "sadness": sum(word in text for word in sadness_words)
    }

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top1 = sorted_scores[0]
    top2 = sorted_scores[1]

    emotion_text = f"{top1[0]} + {top2[0]}"
    confidence_text = f"{top1[1]*50}% + {top2[1]*50}%"

    return {
        "emotion": emotion_text,
        "confidence": confidence_text,
        "scores": scores
    }
