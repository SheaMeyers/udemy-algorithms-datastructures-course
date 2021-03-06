import unittest
from .main import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string_returns_None(self):
        self.assertIsNone(reverse_string('abcd'))

if __name__ == '__main__':
    unittest.main()
