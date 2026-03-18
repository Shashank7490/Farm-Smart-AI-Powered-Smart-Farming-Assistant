"""
translation_service.py
----------------------
Handles all text translation logic for the application.
Falls back gracefully to English if translation fails.
"""

from functools import lru_cache

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None


@lru_cache(maxsize=512)
def translate_text(text: str, language: str) -> str:
    """
    Translates the given text to the selected language.

    Parameters:
        text (str): Text to translate
        language (str): Target language code (e.g., 'en', 'hi', 'ta')

    Returns:
        str: Translated text (or original text if translation fails)
    """

    # Safety checks
    if not text or not isinstance(text, str):
        return text

    if language is None or language.lower() == "en":
        return text

    if GoogleTranslator is None:
        # Translator library not installed
        return text

    try:
        translated = GoogleTranslator(
            source="auto",
            target=language
        ).translate(text)

        return translated if translated else text

    except Exception:
        # Never crash the app due to translation issues
        return text