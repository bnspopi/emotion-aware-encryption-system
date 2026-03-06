from flask import Flask, request, jsonify
from flask_cors import CORS

from encryption import encrypt_message, decrypt_message
from emotion_detector import detect_emotion

app = Flask(__name__)
CORS(app)


# -----------------------------
# Encrypt + Detect Emotion
# -----------------------------
@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    # Detect emotion
    emotion_data = detect_emotion(message)

    # Encrypt message
    encrypted_text = encrypt_message(message)

    return jsonify({
        "encrypted": encrypted_text,
        "emotion": emotion_data["emotion"],
        "confidence": emotion_data["confidence"],
        "scores": emotion_data["scores"]
    })


# -----------------------------
# Decrypt Message
# -----------------------------
@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    encrypted_text = data.get("encrypted")

    if not encrypted_text:
        return jsonify({"error": "No encrypted text provided"}), 400

    try:
        decrypted_message = decrypt_message(encrypted_text)

        return jsonify({
            "decrypted": decrypted_message
        })

    except Exception as e:
        return jsonify({
            "error": "Decryption failed",
            "details": str(e)
        }), 500


# -----------------------------
# Health Check Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Emotion Aware Encryption API Running"
    })


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
