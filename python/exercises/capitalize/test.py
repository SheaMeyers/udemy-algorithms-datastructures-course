import unittest
from .main import capitalize


class TestCapitalize(unittest.TestCase):

    def test_anagrams(self):
      self.assertEqual(capitalize('hi there, how is it going?'), 'Hi There, How Is It Going?')
      self.assertEqual(capitalize('i love breakfast at bill miller bbq'), 'I Love Breakfast At Bill Miller Bbq')


if __name__ == '__main__':
    unittest.main()
