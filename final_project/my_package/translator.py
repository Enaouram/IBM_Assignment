from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class Translator:
    def __init__(self):
        self.authenticator = IAMAuthenticator('BLCXCACU5xg4NVKKvPVlYAQcM_mFk_DzJfLHzRNSoCL1')
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=self.authenticator
        )

        self.language_translator.set_service_url(
            'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/572872b6-5ffc-408f-891f-939ec6bb0242')

    def translate_en_to_fr(self, text):
        translation = self.language_translator.translate(
            text=text,
            source='en',
            target='fr'
        ).get_result()

        return translation['translations'][0]['translation']

    def translate_fr_to_en(self, text):
        translation = self.language_translator.translate(
            text=text,
            source='fr',
            target='en'
        ).get_result()

        return translation['translations'][0]['translation']
