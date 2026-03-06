import React, { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");
  const [encrypted, setEncrypted] = useState("");
  const [emotion, setEmotion] = useState("");
  const [decrypted, setDecrypted] = useState("");

  const encryptMessage = async () => {

    const res = await axios.post("http://localhost:5000/encrypt", {
      message: message
    });

    setEncrypted(res.data.encrypted_text);
    setEmotion(res.data.emotion);
  };

  const decryptMessage = async () => {

    const res = await axios.post("http://localhost:5000/decrypt", {
      encrypted_text: encrypted
    });

    setDecrypted(res.data.decrypted_message);
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

      <button onClick={decryptMessage}>Decrypt</button>

      <h3>Decrypted Message</h3>
      <p>{decrypted}</p>

    </div>
  );
}

export default App;
