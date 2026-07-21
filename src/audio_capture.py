# Voice Translator - Audio Capture Module

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write as write_wav
import sys
import os

# Add parent directory to path so we can import config
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import SAMPLE_RATE, CHANNELS, DTYPE


def record_audio(duration_seconds):
    """Record audio from the microphone for a given duration."""
    print(f"[MIC] Recording for {duration_seconds} seconds...")

    # sd.rec() records audio and returns a numpy array
    # - frames = total number of samples = sample_rate * duration
    # - samplerate = how many samples per second
    # - channels = 1 for mono
    # - dtype = data type of each sample
    audio_data = sd.rec(
        frames=SAMPLE_RATE * duration_seconds,
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE
    )

    # sd.rec() is non-blocking — it starts recording in the background
    # sd.wait() blocks until the recording is finished
    sd.wait()

    print("[MIC] Recording complete.")
    return audio_data


def save_to_wav(audio_data, filename):
    """Save a numpy audio array to a .wav file."""
    write_wav(filename, SAMPLE_RATE, audio_data)
    print(f"[SAVE] Saved to {filename}")


if __name__ == "__main__":
    audio = record_audio(duration_seconds=5)
    save_to_wav(audio, "test_recording.wav")
