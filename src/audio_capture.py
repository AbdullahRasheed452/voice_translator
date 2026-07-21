# Voice Translator - Audio Capture Module

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write as write_wav
import threading
import sys
import os

# Add parent directory to path so we can import config
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from config import SAMPLE_RATE, CHANNELS, DTYPE


def record_audio(duration_seconds):
    """Record audio from the microphone for a fixed duration."""
    print(f"[MIC] Recording for {duration_seconds} seconds...")

    audio_data = sd.rec(
        frames=SAMPLE_RATE * duration_seconds,
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE
    )
    sd.wait()

    print("[MIC] Recording complete.")
    return audio_data


def record_until_stopped():
    """Record audio until the user presses Enter to stop."""
    frames = []
    is_recording = True

    def callback(indata, frame_count, time_info, status):
        """Called for each audio chunk while recording."""
        if is_recording:
            frames.append(indata.copy())

    # Open an input stream that calls our callback for each chunk
    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype=DTYPE,
        blocksize=1024,
        callback=callback
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

    # Concatenate all chunks into one numpy array
    audio_data = np.concatenate(frames)
    return audio_data


def save_to_wav(audio_data, filename):
    """Save a numpy audio array to a .wav file."""
    write_wav(filename, SAMPLE_RATE, audio_data)
    print(f"[SAVE] Saved to {filename}")


if __name__ == "__main__":
    audio = record_until_stopped()
    save_to_wav(audio, "test_recording.wav")

