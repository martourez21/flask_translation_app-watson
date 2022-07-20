"""
This module uses the ibm-watson api to render translations
"""
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
#instantiate a translation object lt
lt = LanguageTranslatorV3(version='2022-07-08', authenticator=authenticator)

#assign your api url to the object
lt.set_service_url(url)

def english_to_french(english_text):
    """
    This function translates string inputs from english to french
    """
    translation = lt.translate(
    english_text,
    model_id='en-fr').get_result()
    data = {}
    for data in translation['translations']:
        print(data['translation'])

    return data['translation']

def french_to_english(french_text):
    """
    This function translates input string from french back to english
    """
    translation = lt.translate(
        french_text,
        model_id='fr-en').get_result()
    data = {}
    for data in translation['translations']:
        print(data['translation'])

    return data['translation']

english_to_french("""Hello! my name is Nestor Martourez,
a full stack application developer. This is the begining 
of my cloud journey...""")

french_to_english("""Bonjour, mon nom est Nestor Martourez,
développeur complet d'applications de pile.
C'est le début de mon voyage en nuage ...""")
