# 🎙️ VoiceFlow AI — Real-Time Voice Translator

Hey there! 👋 This is a real-time voice translation web application built using Python, Flask, OpenAI Whisper, and Web Speech API. 

It lets you speak into your microphone in Urdu, English, Spanish, French, German, or Arabic, streams your spoken words **live on-screen in real-time**, translates them instantly, and speaks the translated output out loud.

---

## ✨ Features

- ⚡ **Real-Time Live Streaming Speech Recognition**: Words appear on screen letter-by-letter as you speak (Google Translate style).
- 🧠 **Urdu Context Prompting**: Fine-tuned context prompt for Pakistani cities (*Faisalabad, Lahore, Karachi, Islamabad*) and common greetings to prevent proper noun hallucinations.
- 🔄 **Smart Auto-Routing**: Automatically detects Hindustani phonemes and routes them to clean Urdu script.
- 🎨 **Electric Blue Web Dashboard**: Built with glassmorphism, animated canvas audio sound waves, instant language swapping (`Urdu ⇄ English`), copy to clipboard buttons, and spacebar shortcuts.
- 📜 **Activity History Drawer**: Keeps track of all your recent translations with timestamps.
- 🔊 **Voice Speech Synthesis**: Plays translated speech back in a natural female voice (`gTTS`).
- 🤖 **Model Fine-Tuning Script**: Includes a complete PyTorch + Hugging Face script to train Whisper on custom Urdu datasets.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.14, Flask, Flask-CORS
- **Speech Recognition**: Web Speech API + OpenAI Whisper (`medium`)
- **Audio Processing**: NumPy, SciPy, SoundDevice, ImageIO-FFmpeg
- **Translation Engine**: `deep-translator` (Google Translate API)
- **Text-to-Speech**: `gTTS` + `playsound`
- **Frontend**: Vanilla HTML5, CSS3 (Electric Blue Dark Mode), JavaScript (Web Speech API + Canvas Visualizer)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/AbdullahRasheed452/voice_translator.git
cd voice_translator
```

### 2. Set up virtual environment
```powershell
py -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Web Application
```bash
python app.py
```

Open **`http://127.0.0.1:5000`** in Google Chrome or Microsoft Edge! 🎤

---

## 📁 Project Structure

```
voice_translator/
├── app.py                      # Flask web server & real-time API
├── config.py                   # Global audio settings (16kHz, mono)
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Web Dashboard (Canvas visualizer, dark UI)
├── src/
│   ├── audio_capture.py        # Sounddevice microphone capture module
│   ├── transcriber.py          # Whisper STT engine & Urdu context prompt
│   ├── translator.py           # Multi-language translation engine
│   ├── tts.py                  # Text-to-speech audio synthesis engine
│   └── pipeline.py             # Standalone CLI terminal runner
└── train/
    └── fine_tune_whisper.py    # PyTorch + HuggingFace Whisper training script
```

---

## 🧑‍💻 Author

Built by [Abdullah Rasheed](https://github.com/AbdullahRasheed452).

## 📄 License

MIT License
