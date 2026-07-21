# Voice Translator - Translation Engine Module

from deep_translator import GoogleTranslator
import sys
import os

# Fix Windows terminal encoding for non-Latin scripts (Hindi, Arabic, etc.)
sys.stdout.reconfigure(encoding='utf-8')  # type: ignore

def translate_text(text, source_lang="auto", target_lang="es"):
    """
    Translate text from a source language to a target language.
    By default, auto-detects the source language and translates to Spanish ('es').
    """
    print(f"[TRANSLATE] Translating from '{source_lang}' to '{target_lang}'...")
    
    # If the text is empty or just whitespace, don't try to translate
    if not text or not text.strip():
        print("[TRANSLATE] Warning: Empty text provided. Nothing to translate.")
        return ""

    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translation = translator.translate(text)
        
        print(f"[TRANSLATE] Original: {text}")
        print(f"[TRANSLATE] Translated: {translation}")
        
        return translation
    except Exception as e:
        print(f"[TRANSLATE] Error during translation: {e}")
        return ""

if __name__ == "__main__":
    # A quick test if we run this file directly
    sample_text = "Hello, my name is Abdullah. I am building a voice translator."
    
    print("--- Test 1: English to Spanish ---")
    translate_text(sample_text, target_lang="es")
    
    print("\n--- Test 2: English to French ---")
    translate_text(sample_text, target_lang="fr")
    
    print("\n--- Test 3: English to Urdu ---")
    translate_text(sample_text, target_lang="ur")
