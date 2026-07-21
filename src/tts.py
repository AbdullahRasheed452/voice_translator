# Voice Translator - Text-to-Speech (TTS) Module

from gtts import gTTS
from playsound import playsound
import os
import sys

# Fix Windows terminal encoding for non-Latin scripts
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

def speak_text(text, lang='en'):
    """
    Convert text to speech and play it through speakers.
    
    Parameters:
    - text (str): The text to speak.
    - lang (str): The language code (default 'en' for English, 'ur' for Urdu, 'es' for Spanish).
    """
    if not text or not text.strip():
        print("[TTS] Warning: Empty text provided. Nothing to speak.")
        return

    temp_audio_file = "temp_tts_audio.mp3"
    print(f"[TTS] Generating speech for: '{text}' (Language: {lang})")

    try:
        # Create the speech object using Google Text-to-Speech
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Save to a temporary mp3 file
        tts.save(temp_audio_file)
        
        # Play the audio out loud
        print("[TTS] Playing audio...")
        playsound(temp_audio_file)
        print("[TTS] Playback finished.")

    except Exception as e:
        print(f"[TTS] Error during text-to-speech: {e}")
        
    finally:
        # Clean up the temporary mp3 file
        if os.path.exists(temp_audio_file):
            try:
                os.remove(temp_audio_file)
            except Exception:
                pass  # Ignore file lock cleanup warnings if playsound holds it briefly


if __name__ == "__main__":
    # Test 1: English
    print("--- Test 1: Speaking English ---")
    speak_text("Hello Abdullah! Your voice translator is now speaking.", lang='en')

    # Test 2: Spanish
    print("\n--- Test 2: Speaking Spanish ---")
    speak_text("Hola, mi nombre es Abdullah.", lang='es')
