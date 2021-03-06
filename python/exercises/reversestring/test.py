import unittest
from .main import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverses_string(self):
        self.assertEqual(reverse_string('abcd'), 'dcba')
    
    def test_reverses_string_with_spaces(self):
        self.assertEqual(reverse_string('  abcd'), 'dcba  ')

if __name__ == '__main__':
    unittest.main()
