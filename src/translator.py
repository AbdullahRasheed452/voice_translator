"""Voice Translator - Translation Engine Module."""

import sys
from deep_translator import GoogleTranslator

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def translate_text(
    text: str,
    source_lang: str = "auto",
    target_lang: str = "en"
) -> str:
    """Translate input text to target language via Google Translate."""
    if not text or not text.strip():
        return ""

    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        return translator.translate(text)
    except Exception:
        return text
