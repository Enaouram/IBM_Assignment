import unittest
from final_project.my_package.translator import Translator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TestTranslator(unittest.TestCase):

    def setUp(self):
        authenticator = IAMAuthenticator('BLCXCACU5xg4NVKKvPVlYAQcM_mFk_DzJfLHzRNSoCL1')
        self.translator = Translator(authenticator)

    def test_french_to_english_translation(self):
        input_text = "Bonjour, comment ça va?"
        expected_output = "Hello, how are you?"
        self.assertEqual(self.translator.translate_fr_to_en(input_text), expected_output)

    def test_french_to_english_translation_not_equal(self):
        input_text = "Je suis un chat."
        expected_output = "I am a cat."
        self.assertNotEqual(self.translator.translate_fr_to_en(input_text), expected_output)

    def test_english_to_french_translation(self):
        input_text = "Hello, how are you?"
        expected_output = "Bonjour, comment ça va?"
        self.assertEqual(self.translator.translate_en_to_fr(input_text), expected_output)

    def test_english_to_french_translation_not_equal(self):
        input_text = "I am a cat."
        expected_output = "Je suis un chat."
        self.assertNotEqual(self.translator.translate_fr_to_en(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()

