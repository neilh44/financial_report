from googletrans import Translator

translator = Translator()

def translate_snippet(text: str, target_language: str = "en") -> str:
    """
    Translates a text snippet into the target language.
    :param text: Text to translate.
    :param target_language: Language code (default: English).
    :return: Translated text.
    """
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        raise ValueError(f"Translation failed: {e}")
