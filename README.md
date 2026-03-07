

https://github.com/user-attachments/assets/06dabfbf-2bab-497f-a2c2-6d1f9c31ec69



https://github.com/user-attachments/assets/eff91568-9bcc-43cc-8687-422ca345c354

# Emotion-Aware Encryption System

## Overview

Emotion-Aware Encryption is a privacy-preserving AI system that allows emotional signals to be detected even when the textual content is encrypted.

Traditional encryption hides both content and emotional meaning. Our system extracts emotional metadata before encryption so that AI systems can interpret user sentiment without accessing the original message.

This architecture demonstrates a new direction in privacy-preserving AI.

---

## Problem

Modern communication systems require:

- Secure encryption
- Emotional understanding
- Privacy preservation

However traditional encryption removes emotional context.

---

## Solution

We propose a pipeline:

User Message
↓
Emotion Detection (NLP)
↓
Emotion Metadata Extraction
↓
AES Encryption
↓
Encrypted Text + Emotion Metadata

---

## Tech Stack

Backend
- Python
- Flask
- Cryptography (AES)

AI
- NLP Rule-based Emotion Detection

Frontend
- React
- Axios

---

## Features

- Secure encryption
- Emotion detection
- Emotion preserved after encryption
- Decryption pipeline
- Web demo interface

---

## Example

Input

"I hate exams"

Output

{
  "encrypted_text": "...",
  "emotion": "anger"
}

---

## Future Work

- Transformer based emotion detection
- Multi-emotion probability detection
- Secure emotion metadata encryption
