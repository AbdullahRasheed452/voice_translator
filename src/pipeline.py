"""Voice Translator - Command-Line Pipeline Runner."""

import os
import sys
from typing import Any

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.audio_capture import record_until_stopped, save_to_wav
from src.transcriber import load_model, transcribe_audio
from src.translator import translate_text
from src.tts import speak_text


def run_single_translation(model: Any) -> None:
    """Execute a single end-to-end terminal voice translation cycle."""
    temp_audio = "temp_pipeline.wav"
    target_lang = "en"

    # 1. Capture Audio
    audio_data = record_until_stopped()
    save_to_wav(audio_data, temp_audio)

    # 2. Transcribe Audio
    print("⏳ Processing...", end="\r")
    transcribed_text, detected_lang = transcribe_audio(model, temp_audio)

    # 3. Translate Text
    translated_text = translate_text(transcribed_text, target_lang=target_lang)

    # Clean up temporary audio file
    if os.path.exists(temp_audio):
        try:
            os.remove(temp_audio)
        except Exception:
            pass

    # Print Clean Output
    print(" " * 30, end="\r")
    print(f"\n🗣️ Spoken ({detected_lang.upper()}): {transcribed_text}")
    print(f"🌍 English:      {translated_text}")

    # 4. Speak Output Out Loud
    if translated_text:
        print("🔊 Speaking...")
        speak_text(translated_text, lang=target_lang)


if __name__ == "__main__":
    print("Starting Voice Translator (High Accuracy Mode)...")
    shared_model = load_model("medium")
    print("✅ Ready!\n")

    try:
        while True:
            run_single_translation(shared_model)
            print("-" * 50)
            choice = input("\n[Enter] to speak again | ['q' + Enter] to quit: ")
            if choice.lower().strip() == "q":
                print("Goodbye!")
                break
    except KeyboardInterrupt:
        print("\nGoodbye!")
