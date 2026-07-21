"""Voice Translator - Text-to-Speech (TTS) Module."""

import os
import sys
import time
from gtts import gTTS
from playsound import playsound

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def speak_text(text: str, lang: str = "en") -> None:
    """Synthesize text into audio speech and play out loud through speakers."""
    if not text or not text.strip():
        return

    temp_audio_file = f"temp_tts_{int(time.time() * 1000)}.mp3"

    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(temp_audio_file)
        playsound(temp_audio_file)
    except Exception:
        pass
    finally:
        if os.path.exists(temp_audio_file):
            try:
                os.remove(temp_audio_file)
            except Exception:
                pass
