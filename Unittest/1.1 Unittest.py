import unittest
import changeText

class testingChangeText(unittest.TestCase):
    def test_upper(self):
        word = 'TEXTO'
        result = changeText.upperText(word)
        self.assertEqual(result, 'TEXTO')

if __name__ == '__main__':
    unittest.main()