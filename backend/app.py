from flask import Flask, request, jsonify
from flask_cors import CORS
from encryption import encrypt_text, decrypt_text
from emotion_detector import detect_emotion

app = Flask(__name__)
CORS(app)


@app.route("/encrypt", methods=["POST"])
def encrypt():

    data = request.json
    message = data["message"]

    emotion, confidence = detect_emotion(message)

    encrypted = encrypt_text(message)

    return jsonify({
        "encrypted": encrypted,
        "emotion": emotion,
        "confidence": confidence
    })


@app.route("/decrypt", methods=["POST"])
def decrypt():

    data = request.json
    encrypted = data["encrypted"]

    decrypted = decrypt_text(encrypted)

    return jsonify({
        "decrypted": decrypted
    })


if __name__ == "__main__":
    app.run(debug=True)
