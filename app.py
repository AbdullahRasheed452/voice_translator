"""Voice Translator - Real-Time Web Backend Server."""

import os
import sys
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

sys.path.append(os.path.dirname(__file__))

from src.translator import translate_text
from src.tts import speak_text

app = Flask(__name__)
CORS(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    """Render the main interactive Web UI dashboard."""
    return render_template("index.html")


@app.route("/api/translate", methods=["POST"])
def api_translate():
    """Real-time translation and voice synthesis endpoint."""
    try:
        data = request.json or {}
        spoken_text = data.get("text", "").strip()
        target_lang = data.get("target_language", "en")

        if not spoken_text:
            return jsonify({"status": "warning", "message": "No text received"}), 400

        translated_text = translate_text(spoken_text, target_lang=target_lang)

        if translated_text:
            speak_text(translated_text, lang=target_lang)

        return jsonify({
            "status": "success",
            "spoken_text": spoken_text,
            "translated_text": translated_text,
            "target_language": target_lang.upper(),
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
