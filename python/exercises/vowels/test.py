import unittest
from .main import vowels


class TestMaxChar(unittest.TestCase):

    def test_vowels_lowercase(self):
      self.assertEqual(vowels('aeiou'), 5)
    
    def test_vowels_uppercase(self):
      self.assertEqual(vowels('AEIOU'), 5)

    def test_vowels_in_alphabet(self):
      self.assertEqual(vowels('abcdefghijklmnopqrstuvwxyz'), 5)
    
    def test_no_vowels(self):
      self.assertEqual(vowels('bcdfghjkl'), 0)

if __name__ == '__main__':
    unittest.main()
