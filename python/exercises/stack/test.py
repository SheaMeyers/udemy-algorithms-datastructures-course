import unittest
from .main import Stack


class TestStack(unittest.TestCase):

    def test_stack(self):
      stack = Stack()
      stack.push(1)
      stack.push(2)
      stack.push(3)
      self.assertEqual(stack.peek(), 3)
      self.assertEqual(stack.pop(), 3)
      self.assertEqual(stack.peek(), 2)
      self.assertEqual(stack.pop(), 2)
      self.assertEqual(stack.peek(), 1)
      self.assertEqual(stack.pop(), 1)
    
    


if __name__ == '__main__':
    unittest.main()
