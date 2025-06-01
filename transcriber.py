import whisper
import os

# Load the model once globally
model = whisper.load_model("base")  # You can also try "small" or "medium" if needed

def transcribe_audio(file_path: str) -> str:
    try:
        result = model.transcribe(file_path)
        text = result["text"]
        lang = result["language"]
        return f"🌐 Detected language: {lang}\n📝 {text}"
    except Exception as e:
        return f"❌ Error during transcription: {e}"
