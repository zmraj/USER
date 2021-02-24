from fridaybot.Configs import Config
from googletrans import LANGUAGES
from google_trans_new import google_translator


async def tr(event, text):
    kk = Config.LANG if LANGUAGES.get(Config.LANG) else 'en'
    if kk == 'en':
        await event.edit(text)
    else:
        final_text = text.replace("*", "").replace("`", "").replace("__", "")
        translator = google_translator()
        translated = translator.translate(final_text, lang_tgt=kk)
        await event.edit(translated)
    return    
