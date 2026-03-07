import React, { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");
  const [encrypted, setEncrypted] = useState("");
  const [emotion, setEmotion] = useState("");
  const [confidence, setConfidence] = useState("");
  const [decrypted, setDecrypted] = useState("");

  const encryptMessage = async () => {

    const res = await axios.post("http://127.0.0.1:5000/encrypt", {
      message: message
    });

    setEncrypted(res.data.encrypted);
    setEmotion(res.data.emotion);
    setConfidence(res.data.confidence);
  };

  const decryptMessage = async () => {

    const res = await axios.post("http://127.0.0.1:5000/decrypt", {
      encrypted: encrypted
    });

    setDecrypted(res.data.decrypted);
  };

  return (
    <div style={{ padding: 40 }}>

      <h1>Emotion Aware Encryption</h1>

      <input
        style={{ width: 400 }}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter message"
      />

      <br/><br/>

      <button onClick={encryptMessage}>Encrypt</button>

      <h3>Encrypted Text</h3>
      <p>{encrypted}</p>

      <h3>Detected Emotion</h3>
      <p>{emotion}</p>

      <h3>Confidence</h3>
      <p>{confidence}</p>

      <button onClick={decryptMessage}>Decrypt</button>

      <h3>Decrypted Message</h3>
      <p>{decrypted}</p>

    </div>
  );
}

export default App;
