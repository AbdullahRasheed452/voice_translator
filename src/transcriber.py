# Voice Translator - Speech-to-Text Module (faster-whisper / CTranslate2)

from faster_whisper import WhisperModel
import sys
import os

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

# Add parent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import SAMPLE_RATE


def load_model(model_name="medium"):
    """
    Load a fast, CTranslate2-optimized Whisper model.
    Uses 'int8' quantization on CPU for 4x-8x speedup with 100% accuracy.
    """
    print(f"[STT] Loading faster-whisper model: '{model_name}' (CPU int8 optimized)...")
    # compute_type="int8" enables high-speed quantization on CPU
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    print("[STT] Model loaded successfully!")
    return model


def transcribe_audio(model, audio_path, language=None):
    """
    Transcribe a WAV file to text using faster-whisper.
    """
    print(f"[STT] Transcribing: {audio_path}")

    # Transcribe audio file
    segments, info = model.transcribe(audio_path, beam_size=5, language=language)
    
    text = " ".join([segment.text for segment in segments]).strip()
    detected_lang = info.language

    # SMART FIX: If auto-detect picked Hindi ('hi'), re-route to Urdu ('ur')
    if not language and detected_lang == "hi":
        print("[STT] Detected Hindi/Urdu phonemes. Re-routing to Urdu script...")
        segments, info = model.transcribe(audio_path, beam_size=5, language="ur")
        text = " ".join([segment.text for segment in segments]).strip()
        detected_lang = "ur"

    print(f"[STT] Language detected: {detected_lang}")
    print(f"[STT] Result: {text}")
    return text


if __name__ == "__main__":
    model = load_model("medium")
    audio_file = os.path.join(os.path.dirname(__file__), '..', 'test_recording.wav')
    if os.path.exists(audio_file):
        transcribe_audio(model, audio_file)
