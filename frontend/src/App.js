import React, { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");
  const [encrypted, setEncrypted] = useState("");
  const [emotion, setEmotion] = useState("");
  const [confidence, setConfidence] = useState(0);
  const [decrypted, setDecrypted] = useState("");

  const encryptMessage = async () => {

    try {

      const res = await axios.post("http://127.0.0.1:5000/encrypt", {
        message: message
      });

      setEncrypted(res.data.encrypted);
      setEmotion(res.data.emotion);
      setConfidence(res.data.confidence);

    } catch (error) {

      console.error(error);
      alert("Encryption failed. Check backend.");

    }
  };

  const decryptMessage = async () => {

  try {

    const res = await axios.post("http://127.0.0.1:5000/decrypt", {
      encrypted: encrypted
    });

    setDecrypted(res.data.decrypted);

  } catch (error) {

    console.log(error);
    alert("Backend not running");

  }

};

  return (
    <div style={{ padding: 40, fontFamily: "Arial" }}>

      <h1>Emotion Aware Encryption</h1>

      <input
        style={{ width: 500, padding: 8 }}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter message"
      />

      <br/><br/>

      <button onClick={encryptMessage}>Encrypt</button>

      <h3>Encrypted Text</h3>
      <p style={{ wordBreak: "break-all" }}>{encrypted}</p>

      <h3>Detected Emotion</h3>
      <p>{emotion}</p>

      <h3>Confidence</h3>

      <div
        style={{
          width: "400px",
          background: "#ddd",
          height: "20px",
          borderRadius: "10px"
        }}
      >
        <div
          style={{
            width: confidence + "%",
            background: "green",
            height: "100%",
            borderRadius: "10px"
          }}
        />
      </div>

      <p>{confidence}%</p>

      <button onClick={decryptMessage}>Decrypt</button>

      <h3>Decrypted Message</h3>
      <p>{decrypted}</p>

    </div>
  );
}

export default App;
