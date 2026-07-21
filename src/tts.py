# Voice Translator - Text-to-Speech (TTS) Module using pyttsx3 (Offline & Instant)

import pyttsx3
import sys

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

def speak_text(text, lang='en'):
    """
    Convert text to speech and play it INSTANTLY through Windows system speakers.
    Uses offline pyttsx3 (SAPI5 on Windows).
    """
    if not text or not text.strip():
        print("[TTS] Warning: Empty text provided. Nothing to speak.")
        return

    print(f"[TTS] Speaking out loud: '{text}'")

    try:
        # Initialize the offline speech engine
        engine = pyttsx3.init()

        # Set speaking rate (speed) - default is ~200, 175 is very natural
        engine.setProperty('rate', 175)

        # Set volume (0.0 to 1.0)
        engine.setProperty('volume', 1.0)

        # Speak and wait until finished
        engine.say(text)
        engine.runAndWait()
        
        # Stop and clean up the engine
        engine.stop()
        print("[TTS] Playback finished.")

    except Exception as e:
        print(f"[TTS] Error during text-to-speech: {e}")


if __name__ == "__main__":
    print("--- Testing Offline TTS ---")
    speak_text("Hello Abdullah! Your voice translator is now instant.", lang='en')
