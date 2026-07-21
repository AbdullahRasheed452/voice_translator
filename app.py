"""Voice Translator - Real-Time Web Backend Server."""

import os
import sys
import subprocess
import logging
from threading import Timer
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

sys.path.append(os.path.dirname(__file__))

from src.translator import translate_text
from src.tts import speak_text

# Silence Flask's default request logging
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.errorhandler(Exception)
def handle_global_exception(e: Exception):
    """Fail-safe global error handler."""
    return jsonify({"status": "error", "message": str(e)}), 200


@app.route("/favicon.ico")
def favicon():
    """Serve favicon to prevent 404 noise."""
    return "", 204


@app.route("/")
def index():
    """Render the main interactive Web UI dashboard."""
    try:
        return render_template("index.html")
    except Exception:
        return "<h1>Loading...</h1><script>setTimeout(()=>location.reload(), 1000)</script>", 200


@app.route("/api/translate", methods=["POST"])
def api_translate():
    """Real-time translation and voice synthesis endpoint."""
    try:
        data = request.json or {}
        spoken_text = data.get("text", "").strip()
        source_lang = data.get("source_language", "auto")
        target_lang = data.get("target_language", "en")

        if not spoken_text:
            return jsonify({"status": "warning", "message": "No text received"}), 200

        translated_text = translate_text(
            text=spoken_text,
            source_lang=source_lang,
            target_lang=target_lang
        )

        if translated_text:
            try:
                speak_text(translated_text, lang=target_lang.split("-")[0])
            except Exception:
                pass

        return jsonify({
            "status": "success",
            "spoken_text": spoken_text,
            "translated_text": translated_text or spoken_text,
            "source_language": source_lang.upper(),
            "target_language": target_lang.upper(),
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 200


def open_browser() -> None:
    """Automatically open default web browser to local server address."""
    try:
        subprocess.Popen('start "" "http://127.0.0.1:5000"', shell=True)
    except Exception:
        try:
            os.startfile("http://127.0.0.1:5000")
        except Exception:
            pass


if __name__ == "__main__":
    print("VoiceFlow AI running at http://127.0.0.1:5000")
    Timer(1.5, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
