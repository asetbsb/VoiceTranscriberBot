import whisper
import os

model = whisper.load_model("base")  

def transcribe_audio(file_path: str) -> str:
    try:
        result = model.transcribe(file_path)
        text = result["text"]
        lang = result["language"]
        return f"🌐 Detected language: {lang}\n📝 {text}"
    except Exception as e:
        return f"❌ Error during transcription: {e}"
