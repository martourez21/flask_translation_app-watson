"""
This module uses the ibm-watson api to render translations
"""
import json
import os
from socket import VM_SOCKETS_INVALID_VERSION
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey2']
url = os.environ['url2']

authenticator = IAMAuthenticator(apikey)
#instantiate a text_to_speech object
text_to_speech = TextToSpeechV1(authenticator=authenticator)
#assign your api url to the object
text_to_speech.set_service_url(url)

def text_to_voice_out(text):
    """
    This function translates string inputs from english to french
    """
    '''with open('./speech.mp3','wb') as audio_file:
        res = text_to_speech.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)
        return res '''
    with open(text, 'r') as f:
        words = f.readlines()
        return words

#text_to_speech("Hello there. My name is Nestor Martourez")