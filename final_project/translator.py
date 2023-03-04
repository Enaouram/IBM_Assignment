from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('BLCXCACU5xg4NVKKvPVlYAQcM_mFk_DzJfLHzRNSoCL1')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/572872b6-5ffc-408f-891f-939ec6bb0242')

