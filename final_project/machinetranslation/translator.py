import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):
    """
    Translate English text to French text.

    :param englishText: The English text to be translated.
    :type englishText: str
    :return: The translated French text.
    :rtype: str
    """
    translation = language_translator.translate(
        text=englishText,
        model_id="en-fr"
    ).get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def french_to_english(frenchText):
    """
    Translate French text to English text.

    :param frenchText: The French text to be translated.
    :type frenchText: str
    :return: The translated English text.
    :rtype: str
    """    
    translation = language_translator.translate(
        text=frenchText,
        model_id="fr-en"
    ).get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
print(english_to_french("Hi"))