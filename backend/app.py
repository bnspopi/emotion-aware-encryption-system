from flask import Flask, request, jsonify
from flask_cors import CORS

from emotion_detector import detect_emotion
from encryption import encrypt_text, decrypt_text

app = Flask(__name__)
CORS(app)

@app.route("/encrypt", methods=["POST"])
def encrypt():

    data = request.json
    message = data["message"]

    emotion = detect_emotion(message)
    encrypted = encrypt_text(message)

    return jsonify({
        "encrypted_text": encrypted.decode(),
        "emotion": emotion
    })


@app.route("/decrypt", methods=["POST"])
def decrypt():

    data = request.json
    encrypted_text = data["encrypted_text"].encode()

    decrypted = decrypt_text(encrypted_text)

    return jsonify({
        "decrypted_message": decrypted
    })


if __name__ == "__main__":
    app.run(debug=True)
