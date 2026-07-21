# Voice Translator - Text-to-Speech (TTS) Module (gTTS - Google Female Voice)

from gtts import gTTS
from playsound import playsound
import time
import os
import sys

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

def speak_text(text, lang='en'):
    """
    Convert text to speech using Google's natural female voice (gTTS)
    and play it through system speakers.
    """
    if not text or not text.strip():
        print("[TTS] Warning: Empty text provided. Nothing to speak.")
        return

    # Use unique filename with timestamp to avoid file lock issues on Windows
    temp_audio_file = f"temp_tts_{int(time.time()*1000)}.mp3"
    print(f"[TTS] Generating female voice speech for: '{text}' (Language: {lang})")

    try:
        # Create speech using Google Text-to-Speech (Natural Female Voice)
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(temp_audio_file)
        
        print("[TTS] Playing audio...")
        playsound(temp_audio_file)
        print("[TTS] Playback finished.")

    except Exception as e:
        print(f"[TTS] Error playing speech: {e}")
        
    finally:
        # Clean up the temporary MP3 file
        if os.path.exists(temp_audio_file):
            try:
                os.remove(temp_audio_file)
            except Exception:
                pass


if __name__ == "__main__":
    print("--- Testing Google Female Voice TTS ---")
    speak_text("Hello Abdullah! This is Google female voice playback.", lang='en')
