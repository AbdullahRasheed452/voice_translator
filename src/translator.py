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
    """Translate input text into target language with multi-stage fallbacks."""
    if not text or not text.strip():
        return ""

    # Clean language code (e.g. 'ur-PK' -> 'ur', 'en-US' -> 'en')
    clean_source = source_lang.split("-")[0].lower() if source_lang else "auto"
    clean_target = target_lang.split("-")[0].lower() if target_lang else "en"

    # If source and target language are the same, return text as-is
    if clean_source == clean_target and clean_source != "auto":
        return text

    try:
        # 1. Primary Translation with explicit source language
        translator = GoogleTranslator(source=clean_source, target=clean_target)
        result = translator.translate(text)
        if result and result.strip():
            return result
    except Exception as err:
        print(f"[TRANSLATE NOTE] Primary source={clean_source} note: {err}")

    try:
        # 2. Fallback Translation with auto-detected source language
        translator = GoogleTranslator(source="auto", target=clean_target)
        result = translator.translate(text)
        if result and result.strip():
            return result
    except Exception as fallback_err:
        print(f"[TRANSLATE NOTE] Auto-detect fallback note: {fallback_err}")

    return text
