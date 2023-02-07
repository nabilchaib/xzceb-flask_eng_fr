import pyOpenSSL
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def translate(text, source_language, target_language):
    # Use a custom context to allow connecting to self-signed SSL certificates
    context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_2_METHOD)
    authenticator = IAMAuthenticator(apikey, ssl_context=context)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    response = language_translator.translate(
        text=text,
        source=source_language,
        target=target_language
    ).get_result()
    return response['translations'][0]['translation']

def english_to_french(english_text):
    """
    Translate English text to French text.

    :param englishText: The English text to be translated.
    :type englishText: str
    :return: The translated French text.
    :rtype: str
    """
    french_text= translate(english_text, "en", "fr")
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English text.

    :param frenchText: The French text to be translated.
    :type frenchText: str
    :return:The translated English text.
    :rtype: str
    """    
    english_text= translate(french_text, "fr", "en")
    return english_text
print(english_to_french("Hi") )
