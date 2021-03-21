import unittest
from .main import max_char


class TestMaxChar(unittest.TestCase):

    def test_max_char(self):
      self.assertEqual(max_char('a'), 'a')
      self.assertEqual(max_char('abcdefghijklmnaaaaa'), 'a')
    
    def test_max_char_with_numbers(self):
      self.assertEqual(max_char('ab1c1d1e1f1g1'), '1')


if __name__ == '__main__':
    unittest.main()
