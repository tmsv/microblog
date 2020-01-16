import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language, auth):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error1: the translation service is not configured.')
    
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json'
        '/translate?text={}&lang={}-{}&key={}'.format(
            text, source_language, dest_language, auth))
    if r.status_code != 200:
        return _('Error: the translation service failed.')

    response = json.loads(r.content.decode('utf-8-sig'))

    return response['text'][0]