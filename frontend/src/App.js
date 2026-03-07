import React, { useState } from "react"
import { encryptMessage, decryptMessage } from "./api"

export default function App(){

  const [text,setText] = useState("")
  const [cipher,setCipher] = useState("")
  const [emotion,setEmotion] = useState("")
  const [original,setOriginal] = useState("")

  const encrypt = async () => {

    if(!text) return

    const res = await encryptMessage(text)

    setCipher(res.encrypted_text)
    setEmotion(res.emotion)
  }

  const decrypt = async () => {

    if(!cipher) return

    const res = await decryptMessage(cipher)

    setOriginal(res.original_message)
    setEmotion(res.emotion)
  }

  return (

    <div style={{padding:40,fontFamily:"Arial"}}>

      <h1>Emotion Cipher 🔐</h1>

      <textarea
        rows="5"
        cols="60"
        placeholder="Enter your message..."
        onChange={(e)=>setText(e.target.value)}
      />

      <br/><br/>

      <button onClick={encrypt}>Encrypt Message</button>

      <h3>Encrypted Text</h3>
      <p>{cipher}</p>

      <h3>Detected Emotion</h3>
      <p>{emotion}</p>

      <button onClick={decrypt}>Decrypt Message</button>

      <h3>Original Message</h3>
      <p>{original}</p>

    </div>
  )
}
