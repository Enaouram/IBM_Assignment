import unittest
from translator import LanguageTranslator

class TestLanguageTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = LanguageTranslator()

    def test_frenchToEnglish(self):
        result = self.translator.frenchToEnglish("Bonjour")
        self.assertEqual(result, "Hello")
        self.assertNotEqual(result, "Bonjour")

    def test_englishToFrench(self):
        result = self.translator.englishToFrench("Hello")
        self.assertEqual(result, "Bonjour")
        self.assertNotEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
