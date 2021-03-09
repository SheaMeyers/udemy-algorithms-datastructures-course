import unittest
from .main import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_aba(self):
        self.assertTrue(is_palindrome('aba'))
    
    def test_aba_with_space_at_beginning(self):
        self.assertFalse(is_palindrome(' aba'))
    
    def test_aba_with_space_at_end(self):
        self.assertFalse(is_palindrome('aba '))
    
    def test_greeting(self):
        self.assertFalse(is_palindrome('greeting'))
    
    def test_1000000001(self):
        self.assertTrue(is_palindrome('1000000001'))

    def test_two_words_with_different_cases(self):
        self.assertFalse(is_palindrome('Fish hsif'))

    def test_pennep(self):
        self.assertTrue(is_palindrome('pennep'))

if __name__ == '__main__':
    unittest.main()
