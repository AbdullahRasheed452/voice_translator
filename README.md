# 🎙️ VoiceFlow AI

VoiceFlow AI is a real-time voice translation web application built with Python, Flask, OpenAI Whisper, and the Web Speech API. 

It allows you to speak into your microphone in Urdu, English, Spanish, French, German, or Arabic, stream your spoken words live on-screen in real time, translate them instantly, and listen to the translated audio output.

---

## ✨ Key Features

- ⚡ **Real-Time Speech Recognition**: Words stream on-screen letter-by-letter as you speak.
- 🎯 **Multi-Language Support**: Seamless translation between Urdu, English, Spanish, French, German, and Arabic.
- 🎨 **Electric Blue Web UI**: Modern dark-mode dashboard with interactive 3D parallax tilt effects, animated soundwave visualizer, spacebar shortcuts, and language swap (`Urdu ⇄ English`).
- 📜 **Recent Activity Drawer**: Maintains a history of your translations with timestamps.
- 🔊 **Text-to-Speech Synthesis**: Automatically plays translated text back in natural audio using `gTTS`.
- 🛡️ **Fail-Safe Crash Protection**: Global error handling in both Python and JavaScript to ensure maximum runtime stability.
- 🤖 **Whisper Model Fine-Tuning**: Includes a custom training script to fine-tune Whisper models on specific datasets.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Flask-CORS
- **Speech Recognition**: Web Speech API + OpenAI Whisper (`medium`)
- **Translation Engine**: `deep-translator` (Google Translate)
- **Audio & TTS**: `gTTS`, `playsound`, `sounddevice`, `imageio-ffmpeg`
- **Frontend**: HTML5, Vanilla CSS3 (Custom Design System), JavaScript

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/AbdullahRasheed452/voice_translator.git
cd voice_translator
```

### 2. Set Up Virtual Environment
```powershell
py -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Web Application
```bash
python app.py
```

Running `python app.py` will launch the Flask web server and automatically redirect you to **`http://127.0.0.1:5000`** in your browser.

---

## 📁 Project Structure

```
voice_translator/
├── app.py                      # Flask web server & real-time API routes
├── config.py                   # Audio configuration parameters
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Interactive Web UI dashboard
├── src/
│   ├── audio_capture.py        # Sounddevice microphone capture module
│   ├── transcriber.py          # Whisper STT engine & Urdu context prompt
│   ├── translator.py           # Multi-language translation engine
│   ├── tts.py                  # Text-to-speech audio synthesis engine
│   └── pipeline.py             # Standalone CLI pipeline runner
└── train/
    └── fine_tune_whisper.py    # PyTorch + HuggingFace Whisper training script
```

---

## 🧑‍💻 Author

Built by [Abdullah Rasheed](https://github.com/AbdullahRasheed452).

