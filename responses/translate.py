import six
from google.cloud import translate_v2 as translate
import os, pycountry

def get_lang_code(lang: str) -> str:
    """Get the ISO 639-1 language code for a given language by name."""
    res = pycountry.languages.get(name=lang)
    return res.alpha_2

def translate_message(translate_str: str) -> str:
    """Translate a message to another language."""
    splits = translate_str.split(' -> ')
    lang = get_lang_code(splits[1])
    text = splits[0]
    translated = translate_text(lang, text)
    return u"\"{}\" in {} is: {}".format(text, lang, translated)

def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    return result["translatedText"]
