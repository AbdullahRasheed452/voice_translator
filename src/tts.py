# Voice Translator - Text-to-Speech (TTS) Module

import win32com.client
import pythoncom
import subprocess
import sys

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

def speak_text(text, lang='en'):
    """
    Convert text to speech and play it out loud.
    Uses Windows native SAPI5 voice engine via COM.
    """
    if not text or not text.strip():
        print("[TTS] Warning: Empty text provided. Nothing to speak.")
        return

    print(f"[TTS] Speaking out loud: '{text}'")

    try:
        # Initialize Windows COM library for thread-safe audio dispatching
        pythoncom.CoInitialize()
        
        # Dispatch native Windows SAPI.SpVoice engine
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # Adjust speaking rate (-10 to 10, default 0)
        speaker.Rate = 1
        
        # Speak synchronously through default audio output
        speaker.Speak(text)
        print("[TTS] Playback finished.")
        return

    except Exception as e:
        print(f"[TTS] SAPI note: {e}, falling back to PowerShell Speech...")

    # Fallback using PowerShell System.Speech
    try:
        clean_text = text.replace('"', '\\"')
        ps_cmd = f"Add-Type -AssemblyName System.Speech; `$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; `$synth.Speak('{clean_text}')"
        subprocess.run(["powershell", "-Command", ps_cmd], check=True)
        print("[TTS] Playback finished via PowerShell.")
    except Exception as err:
        print(f"[TTS] Error playing speech: {err}")


if __name__ == "__main__":
    print("--- Testing Native SAPI Speech ---")
    speak_text("Hello Abdullah! This is native Windows speech playback.", lang='en')
