from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from encryption import encrypt_message, decrypt_message
from emotion import detect_emotion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

class Cipher(BaseModel):
    cipher: str

@app.post("/encrypt")
def encrypt(msg: Message):

    emotion = detect_emotion(msg.text)

    encrypted = encrypt_message(msg.text)

    return {
        "encrypted_text": encrypted,
        "emotion": emotion
    }

@app.post("/decrypt")
def decrypt(data: Cipher):

    original = decrypt_message(data.cipher)

    emotion = detect_emotion(original)

    return {
        "original_message": original,
        "emotion": emotion
    }
