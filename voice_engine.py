from gtts import gTTS
import os

def text_to_speech(text: str, lang: str = "en") -> str:
    output_path = "uploads/response.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)
    return output_path