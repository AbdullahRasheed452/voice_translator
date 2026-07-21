# Voice Translator - Speech-to-Text Module (Whisper)

import whisper
import numpy as np
from scipy.io.wavfile import read as read_wav
import sys
import os

# Add parent directory to path so we can import config
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import SAMPLE_RATE


def load_model(model_name="base"):
    """Load a Whisper speech-to-text model."""
    print(f"[STT] Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)
    print("[STT] Model loaded.")
    return model


def transcribe_audio(model, audio_path):
    """Transcribe a WAV file to text using the loaded Whisper model."""
    print(f"[STT] Transcribing: {audio_path}")

    # Load WAV file ourselves using scipy (avoids needing ffmpeg)
    sample_rate, audio_data = read_wav(audio_path)

    # Whisper expects a 1D float32 numpy array with values between -1 and 1
    # Our WAV is int16 (-32768 to 32767), so we convert:
    audio_float = audio_data.astype(np.float32) / 32768.0

    # If stereo, take only the first channel
    if audio_float.ndim > 1:
        audio_float = audio_float[:, 0]

    # model.transcribe() returns a dictionary with keys:
    #   "text"     - the full transcribed text
    #   "segments" - list of segments with timestamps
    #   "language" - detected language
    result = model.transcribe(audio_float, fp16=False)

    text = result["text"].strip()
    language = result.get("language", "unknown")

    print(f"[STT] Language detected: {language}")
    print(f"[STT] Result: {text}")
    return text


if __name__ == "__main__":
    # Load the model
    model = load_model("base")

    # Transcribe the test recording from Day 1
    audio_file = os.path.join(os.path.dirname(__file__), '..', 'test_recording.wav')

    if not os.path.exists(audio_file):
        print("[STT] Error: test_recording.wav not found.")
        print("[STT] Run audio_capture.py first to create a recording.")
        sys.exit(1)

    text = transcribe_audio(model, audio_file)
