from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class Translator:
    """
    A class that provides translation services from English to
     French and vice versa, using IBM Watson Language Translator API.

    Attributes:
        authenticator (IAMAuthenticator): An instance of the
        IAMAuthenticator class to authenticate with the IBM Watson API.
        language_translator (LanguageTranslatorV3): An instance of
        the LanguageTranslatorV3 class to perform translation.
    """

    def __init__(self):
        """
        Constructor method for the Translator class.
        Initializes the authenticator and language_translator attributes.
        """
        self.authenticator = IAMAuthenticator('BLCXCACU5xg4NVKKvPVlYAQcM_mFk_DzJfLHzRNSoCL1')
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=self.authenticator
        )
        self.language_translator.set_service_url(
            'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/' +
            '572872b6-5ffc-408f-891f-939ec6bb0242'
        )

    def translate_en_to_fr(self, text):
        """
        Translates English text to French.

        Args:
            text (str): The English text to be translated.

        Returns:
            str: The translated French text.
        """
        translation = self.language_translator.translate(
            text=text,
            source='en',
            target='fr'
        ).get_result()

        return translation['translations'][0]['translation']

    def translate_fr_to_en(self, text):
        """
        Translates French text to English.

        Args:
            text (str): The French text to be translated.

        Returns:
            str: The translated English text.
        """
        translation = self.language_translator.translate(
            text=text,
            source='fr',
            target='en'
        ).get_result()

        return translation['translations'][0]['translation']

