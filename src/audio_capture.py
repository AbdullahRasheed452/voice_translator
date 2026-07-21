# ──────────────────────────────────────────────
# YOUR TASK: Implement the audio capture module
# ──────────────────────────────────────────────
#
# You need to write:
#
# 1) record_audio(duration_seconds)
#    - Records audio from the microphone for the given duration
#    - Returns a numpy array of audio data
#    - Hint: look at sounddevice.rec() — it records and returns a numpy array
#
# 2) save_to_wav(audio_data, filename)
#    - Takes the numpy array and writes it to a .wav file
#    - Hint: scipy.io.wavfile.write() does this in one line
#
# 3) A __main__ block that records 5 seconds
#    and saves it as 'test_recording.wav'
#
# Imports you'll need:
#   import sounddevice as sd
#   import numpy as np
#   from scipy.io.wavfile import write as write_wav
#   import sys, os
#   sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#   from config import SAMPLE_RATE, CHANNELS, DTYPE
#
# Expected output when you run this file:
#   🎤 Recording for 5 seconds...
#   🎤 Recording complete.
#   💾 Saved to test_recording.wav
#
# Good luck! 🎤
# ──────────────────────────────────────────────
