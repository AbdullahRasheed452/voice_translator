# Voice Translator - Text-to-Speech (TTS) Module

import pyttsx3
import subprocess
import sys

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

def speak_text(text, lang='en'):
    """
    Convert text to speech and play it through Windows system speakers.
    Uses pyttsx3 with Windows System.Speech PowerShell fallback.
    """
    if not text or not text.strip():
        print("[TTS] Warning: Empty text provided. Nothing to speak.")
        return

    print(f"[TTS] Speaking out loud: '{text}'")

    # Try pyttsx3 first
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 165)
        engine.say(text)
        engine.runAndWait()
        print("[TTS] Playback finished.")
        return
    except Exception as e:
        print(f"[TTS] pyttsx3 note: {e}, using system speech synthesizer...")

    # Reliable Windows PowerShell System.Speech fallback
    try:
        # Escape double quotes for PowerShell
        clean_text = text.replace('"', '\\"')
        ps_command = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{clean_text}")'
        subprocess.run(["powershell", "-Command", ps_command], check=True)
        print("[TTS] Playback finished via System.Speech.")
    except Exception as e:
        print(f"[TTS] Error playing speech: {e}")


if __name__ == "__main__":
    print("--- Testing Speech ---")
    speak_text("Hello Abdullah! Voice translator audio check.", lang='en')
