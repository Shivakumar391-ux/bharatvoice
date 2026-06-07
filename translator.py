from deep_translator import GoogleTranslator

def translate_to_english(text: str, source_lang: str) -> str:
    return GoogleTranslator(
        source=source_lang,
        target='english'
    ).translate(text)

def translate_to_local(text: str, target_lang: str) -> str:
    return GoogleTranslator(
        source='english',
        target=target_lang
    ).translate(text)