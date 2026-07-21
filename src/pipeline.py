# Voice Translator - Main Pipeline

import os
import sys

# Add parent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import our custom modules
from src.audio_capture import record_until_stopped, save_to_wav
from src.transcriber import load_model, transcribe_audio
from src.translator import translate_text
from src.tts import speak_text

def run_pipeline():
    """Runs the full voice translation pipeline."""
    temp_audio_file = "temp_pipeline_audio.wav"
    target_language = "en" # Translate everything to English

    print("\n" + "="*50)
    print("🎙️ REAL-TIME VOICE TRANSLATOR PIPELINE 🎙️")
    print("="*50 + "\n")

    # ---------------------------------------------------------
    # TODO 1: Capture Audio
    # ---------------------------------------------------------
    print("[PIPELINE] Step 1: Ready to record...")
    audio_data = record_until_stopped()
    save_to_wav(audio_data, temp_audio_file)

    # ---------------------------------------------------------
    # TODO 2: Transcribe Audio
    # ---------------------------------------------------------
    print("\n[PIPELINE] Step 2: Transcribing...")
    model = load_model("small")
    transcribed_text = transcribe_audio(model, temp_audio_file)

    # ---------------------------------------------------------
    # TODO 3: Translate Text
    # ---------------------------------------------------------
    print("\n[PIPELINE] Step 3: Translating...")
    translated_text = translate_text(transcribed_text, target_lang=target_language)

    # ---------------------------------------------------------
    # TODO 4: Speak Translated Text (TTS)
    # ---------------------------------------------------------
    print("\n[PIPELINE] Step 4: Speaking translation...")
    speak_text(translated_text, lang=target_language)

    # ---------------------------------------------------------
    # TODO 5: Clean up
    # ---------------------------------------------------------
    print("\n[PIPELINE] Step 5: Cleaning up...")
    if os.path.exists(temp_audio_file):
        os.remove(temp_audio_file)
        print(f"[PIPELINE] Deleted temporary file: {temp_audio_file}")
    

    print("\n✅ Pipeline complete!")


if __name__ == "__main__":
    run_pipeline()
