from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from translator import translate_to_english, translate_to_local
from ai_engine import get_ai_response
from voice_engine import text_to_speech

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(
    user_text: str = Form(...),
    language: str = Form(default="en")
):
    english_text = translate_to_english(user_text, language)
    ai_response = get_ai_response(english_text)
    local_response = translate_to_local(ai_response, language)
    audio_path = text_to_speech(local_response, language)

    return {
        "original_text": user_text,
        "ai_response": local_response,
        "audio": "/audio"
    }

@app.get("/audio")
def get_audio():
    return FileResponse("uploads/response.mp3",
                        media_type="audio/mpeg")