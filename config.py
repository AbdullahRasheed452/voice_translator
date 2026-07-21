# ──────────────────────────────────────────────
# Voice Translator — Audio Configuration
# ──────────────────────────────────────────────

import numpy as np

# Sample rate in Hz — 16kHz is the standard for speech recognition models
SAMPLE_RATE = 16000

# Mono audio — single channel is all we need for speech
CHANNELS = 1

# Number of samples read per chunk
CHUNK_SIZE = 1024

# Audio data type — 16-bit integer (2 bytes per sample)
DTYPE = np.int16
