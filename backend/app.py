from flask import Flask, request, jsonify
from flask_cors import CORS
from encryption import encrypt_message, decrypt_message
from emotion_detector import detect_emotion

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Emotion Aware Encryption API Running"

@app.route("/encrypt", methods=["POST"])
def encrypt():

    data = request.json
    message = data.get("message")

    emotion_data = detect_emotion(message)

    encrypted_text = encrypt_message(message)

    return jsonify({
        "encrypted": encrypted_text,
        "emotion": emotion_data["emotion"],
        "confidence": emotion_data["confidence"]
    })

@app.route("/decrypt", methods=["POST"])
def decrypt():

    data = request.json
    encrypted = data.get("encrypted")

    decrypted_text = decrypt_message(encrypted)

    return jsonify({
        "decrypted": decrypted_text
    })

if __name__ == "__main__":
    app.run(debug=True)
