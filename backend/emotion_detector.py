def detect_emotion(text):

    text = text.lower()

    joy_words = [
        "ecstatic","happy","excited","love","great","joy",
        "thrilled","delighted","amazing","wonderful"
    ]

    anxiety_words = [
        "anxious","nervous","deadline","stress",
        "worried","fear","concern","pressure"
    ]

    anger_words = [
        "hate","angry","mad","furious","annoyed"
    ]

    sadness_words = [
        "sad","depressed","cry","upset","lonely"
    ]

    scores = {
        "Joy": sum(word in text for word in joy_words),
        "Anxiety": sum(word in text for word in anxiety_words),
        "Anger": sum(word in text for word in anger_words),
        "Sadness": sum(word in text for word in sadness_words)
    }

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top1 = sorted_scores[0]
    top2 = sorted_scores[1]

    emotion = f"{top1[0]} + {top2[0]}"
    confidence = int((top1[1] + top2[1]) * 25)

    return emotion, confidence
