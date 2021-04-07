import unittest
from .main import is_anagram


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
      self.assertTrue(is_anagram('hello', 'llohe'))
      self.assertTrue(is_anagram('Whoa! Hi!', 'Hi! Whoa!'))
      self.assertFalse(is_anagram('One One', 'Two two two'))
      self.assertFalse(is_anagram('One one', 'One one c'))
      self.assertFalse(is_anagram('A tree, a life, a bench', 'A tree, a fence, a yard'))


if __name__ == '__main__':
    unittest.main()
