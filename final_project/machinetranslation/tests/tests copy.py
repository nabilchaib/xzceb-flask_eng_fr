import unittest
from translator import french_to_english, english_to_french

class TranslatorTestCase(unittest.TestCase):
    def test_english_to_french_null_input(self):
        self.assertEqual(english_to_french(None), None)

    def test_french_to_english_null_input(self):
        self.assertEqual(french_to_english(None), None)

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
