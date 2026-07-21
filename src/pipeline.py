# Voice Translator - Main Pipeline (High Speed & High Accuracy)

import os
import sys

# Add parent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import our custom modules
from src.audio_capture import record_until_stopped, save_to_wav
from src.transcriber import load_model, transcribe_audio
from src.translator import translate_text
from src.tts import speak_text

def run_pipeline(model=None):
    """Runs the full voice translation pipeline."""
    temp_audio_file = "temp_pipeline_audio.wav"
    target_language = "en" # Translate everything to English

    # Load model once if not already passed in
    if model is None:
        model = load_model("medium")

    print("\n" + "="*50)
    print("🎙️ REAL-TIME VOICE TRANSLATOR PIPELINE 🎙️")
    print("="*50 + "\n")

    # Step 1: Capture Audio
    print("[PIPELINE] Step 1: Ready to record...")
    audio_data = record_until_stopped()
    save_to_wav(audio_data, temp_audio_file)

    # Step 2: High Speed Transcription (faster-whisper)
    print("\n[PIPELINE] Step 2: Transcribing (High Speed)...")
    transcribed_text = transcribe_audio(model, temp_audio_file)

    # Step 3: Translate Text
    print("\n[PIPELINE] Step 3: Translating...")
    translated_text = translate_text(transcribed_text, target_lang=target_language)

    # Step 4: Speak Translated Text (gTTS Female Voice)
    print("\n[PIPELINE] Step 4: Speaking translation...")
    speak_text(translated_text, lang=target_language)

    # Step 5: Clean up
    print("\n[PIPELINE] Step 5: Cleaning up...")
    if os.path.exists(temp_audio_file):
        try:
            os.remove(temp_audio_file)
            print(f"[PIPELINE] Deleted temporary file: {temp_audio_file}")
        except Exception:
            pass

    print("\n✅ Pipeline complete!")


if __name__ == "__main__":
    # Pre-load model ONCE at startup so pipeline runs at lightning speed
    print("Initializing Voice Translator Engine...")
    shared_model = load_model("medium")
    
    # Run the pipeline
    run_pipeline(shared_model)
