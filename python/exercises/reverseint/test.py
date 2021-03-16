import unittest
from .main import reverse_int

class TestReverseInt(unittest.TestCase):

    def test_reverses_int_handles_0(self):
        self.assertEqual(reverse_int(0), 0)
    
    def test_reverses_int_with_positive_numbers(self):
        self.assertEqual(reverse_int(5), 5)
        self.assertEqual(reverse_int(15), 51)
        self.assertEqual(reverse_int(90), 9)
        self.assertEqual(reverse_int(2359), 9532)
    
    def test_reverses_int_with_negative_numbers(self):
        self.assertEqual(reverse_int(-5), -5)
        self.assertEqual(reverse_int(-15), -51)
        self.assertEqual(reverse_int(-90), -9)
        self.assertEqual(reverse_int(-2359), -9532)

if __name__ == '__main__':
    unittest.main()
