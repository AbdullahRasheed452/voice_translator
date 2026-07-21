"""Voice Translator - Audio Capture Module."""

import os
import sys
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write as write_wav

# Add parent directory to path to import config
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from config import CHANNELS, DTYPE, SAMPLE_RATE


def record_audio(duration_seconds: int) -> np.ndarray:
    """Record microphone audio for a fixed duration of seconds."""
    print(f"[MIC] Recording for {duration_seconds} seconds...")
    audio_data = sd.rec(
        frames=SAMPLE_RATE * duration_seconds,
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE,
    )
    sd.wait()
    print("[MIC] Recording complete.")
    return audio_data


def record_until_stopped() -> np.ndarray:
    """Record microphone audio until user presses Enter to stop."""
    frames: list[np.ndarray] = []
    is_recording = True

    def callback(indata, frame_count, time_info, status):
        if is_recording:
            frames.append(indata.copy())

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE,
        blocksize=1024,
        callback=callback,
    )

    print("[MIC] Press Enter to START recording...")
    input()

    stream.start()
    print("[MIC] Recording... Press Enter to STOP.")
    input()

    is_recording = False
    stream.stop()
    stream.close()

    print("[MIC] Recording complete.")
    return np.concatenate(frames)


def save_to_wav(audio_data: np.ndarray, filename: str) -> None:
    """Save raw NumPy audio array to a standard 16-bit PCM WAV file."""
    write_wav(filename, SAMPLE_RATE, audio_data)
    print(f"[SAVE] Saved audio file: {filename}")


if __name__ == "__main__":
    audio = record_until_stopped()
    save_to_wav(audio, "test_recording.wav")
