import unittest
from .main import matrix

class TestPalindrome(unittest.TestCase):

    def test_2_by_2(self):
        self.assertEqual(matrix(2), 
                        [[1, 2],
                         [4, 3]])
    
    def test_3_by_3(self):
        self.assertEqual(matrix(3), 
                        [[1, 2, 3],
                         [8, 9, 4],
                         [7, 6, 5]])

    def test_4_by_4(self):
        self.assertEqual(matrix(4), 
                        [[1,   2,  3, 4],
                         [12, 13, 14, 5],
                         [11, 16, 15, 6],
                         [10,  9,  8, 7]])


if __name__ == '__main__':
    unittest.main()
