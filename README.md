# 🌍 Real-Time AI Voice Translator

A production-quality real-time voice translator that captures speech, transcribes it, translates it to another language, and speaks the translation back — all in real time.

## 🏗️ Architecture

```
🎤 Microphone  →  🗣️ Speech-to-Text  →  🌍 Translation  →  🔊 Text-to-Speech  →  🔈 Speaker
   (Audio)          (Whisper)             (AI Engine)        (TTS Engine)          (Output)
```

## 🚀 Features (In Progress)

- [ ] Real-time microphone audio capture
- [ ] Speech-to-Text using OpenAI Whisper
- [ ] Language translation engine
- [ ] Text-to-Speech output
- [ ] User interface
- [ ] Multi-language support

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.14 |
| Audio Capture | sounddevice + numpy |
| Audio Processing | scipy |
| Speech-to-Text | OpenAI Whisper (coming soon) |
| Translation | TBD |
| Text-to-Speech | TBD |

## 📦 Setup

```bash
# Clone the repository
git clone https://github.com/AbdullahRasheed452/voice_translator.git
cd voice_translator

# Create virtual environment
py -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📁 Project Structure

```
voice_translator/
├── config.py              # Audio configuration constants
├── requirements.txt       # Python dependencies
├── pyrightconfig.json     # IDE type checking config
├── src/
│   └── audio_capture.py   # Microphone audio capture module
└── tests/
    └── ...                # Unit tests
```

## 🧑‍💻 Author

Built by [Abdullah Rasheed](https://github.com/AbdullahRasheed452) as a hands-on AI/ML engineering project.

## 📄 License

MIT
