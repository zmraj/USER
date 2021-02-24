#    Copyright (C) @DevsExpo 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from fridaybot.Configs import Config
from googletrans import LANGUAGES
from google_trans_new import google_translator

def tr_engine(text="Confused Bonking Face."):
    kk = Config.LANG if LANGUAGES.get(Config.LANG) else 'en'
    if kk == 'en':
        hmm = text
    else:
        try:
            translator = google_translator()
            translated = translator.translate(text, lang_tgt=kk)
            hmm = translated
        except:
            hmm = text
    return hmm
