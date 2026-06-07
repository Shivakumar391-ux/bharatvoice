from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_response(user_text: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant for rural and elderly Indian citizens. Answer in very simple, short and clear language."
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"