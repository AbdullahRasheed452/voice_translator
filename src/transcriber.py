"""Voice Translator - Speech-to-Text (STT) Module."""

import os
import sys
from typing import Any
import imageio_ffmpeg
import numpy as np
from scipy.io.wavfile import read as read_wav
import whisper

# Reconfigure stdout for UTF-8 non-Latin script printing on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Register bundled ffmpeg binary into environment PATH
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)
if ffmpeg_dir not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + ffmpeg_dir


def load_model(model_name: str = "medium") -> Any:
    """Load OpenAI Whisper Speech-to-Text model into memory."""
    return whisper.load_model(model_name)


def transcribe_audio(
    model: Any,
    audio_path: str,
    language: str | None = None
) -> tuple[str, str]:
    """Transcribe audio file into text with Urdu context prompting and auto-routing."""
    try:
        sample_rate, audio_data = read_wav(audio_path)
        audio_float = audio_data.astype(np.float32) / 32768.0
        if audio_float.ndim > 1:
            audio_float = audio_float[:, 0]
    except Exception:
        audio_float = audio_path

    # Context prompt for Pakistani cities, names, and greetings
    urdu_context_prompt = (
        "اردو گفتگو: پاکستان، فیصل آباد، لاہور، کراچی، اسلام آباد، "
        "میرا نام، آپ کا نام، کیا حال ہے، میں ٹھیک ہوں، شکریہ۔"
    )

    kwargs: dict[str, Any] = {
        "fp16": False,
        "temperature": 0.0,
        "beam_size": 5,
        "initial_prompt": urdu_context_prompt,
    }

    if language:
        kwargs["language"] = language

    result = model.transcribe(audio_float, **kwargs)
    detected_lang: str = result.get("language", "unknown")

    # Smart auto-route Hindi predictions to Urdu script
    if not language and detected_lang == "hi":
        kwargs["language"] = "ur"
        result = model.transcribe(audio_float, **kwargs)
        detected_lang = "ur"

    text: str = result["text"].strip()
    return text, detected_lang
