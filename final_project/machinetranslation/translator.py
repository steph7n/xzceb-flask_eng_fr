'''
This module provides translation from English to French and vice versa
using IBM Watson Translation Service
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.getenv("apikey")
url = os.getenv("url")
ver = os.getenv("version")

auth = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = ver,
    authenticator = auth
)

language_translator.set_service_url(url)

language_translator.set_default_headers({'x-watson-learning-opt-out':"true"})

def english_to_french(english_text):
    '''
    Translate english text to french
    '''
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    '''
    Translate french text to english
    '''
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]
