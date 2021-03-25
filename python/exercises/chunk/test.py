import unittest
from .main import chunk


class TestChunk(unittest.TestCase):

    def test_chunk_1(self):
      array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

      result = chunk(array, 2)
      
      self.assertEqual(result, [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    
    def test_chunk_2(self):
      array = [1, 2, 3]

      result = chunk(array, 1)
      
      self.assertEqual(result, [[1], [2], [3]])
    
    def test_chunk_3(self):
      array = [1, 2, 3]

      result = chunk(array, 1)
      
      self.assertEqual(result, [[1], [2], [3]])
    
    def test_chunk_4(self):
      array = [1, 2, 3, 4, 5]

      result = chunk(array, 3)
      
      self.assertEqual(result, [[1, 2, 3], [4, 5]])
    
    def test_chunk_5(self):
      array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

      result = chunk(array, 5)
      
      self.assertEqual(result, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]])


if __name__ == '__main__':
    unittest.main()
