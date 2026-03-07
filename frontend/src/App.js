import React, { useState } from "react";
import { encryptMessage, decryptMessage } from "./api";

export default function App() {

  const [text, setText] = useState("");
  const [cipher, setCipher] = useState("");
  const [emotion, setEmotion] = useState("");
  const [original, setOriginal] = useState("");

  const encrypt = async () => {

    const res = await encryptMessage(text);

    setCipher(res.encrypted_text);
    setEmotion(res.emotion);
  };

  const decrypt = async () => {

    const res = await decryptMessage(cipher);

    setOriginal(res.original_message);
    setEmotion(res.emotion);
  };

  return (

    <div style={{padding:40,fontFamily:"Arial"}}>

      <h1>Mini Emotion Cipher</h1>

      <textarea
        rows="4"
        cols="60"
        placeholder="Enter message..."
        onChange={(e)=>setText(e.target.value)}
      />

      <br/><br/>

      <button onClick={encrypt}>Encrypt</button>

      <h3>Encrypted Text</h3>
      <p>{cipher}</p>

      <h3>Detected Emotion</h3>
      <p>{emotion}</p>

      <button onClick={decrypt}>Decrypt</button>

      <h3>Original Message</h3>
      <p>{original}</p>

    </div>
  );
}
