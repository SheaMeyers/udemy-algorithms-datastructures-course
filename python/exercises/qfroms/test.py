import unittest
from .main import Queue


class TestQueue(unittest.TestCase):

    def test_order_maintained(self):
      queue = Queue()
      queue.add(1)
      queue.add(2)
      queue.add(3)
      self.assertEqual(queue.remove(), 1)
      self.assertEqual(queue.remove(), 2)
      self.assertEqual(queue.remove(), 3)
    
    def test_peak_does_not_remove(self):
      queue = Queue()
      queue.add(1)
      queue.add(2)
      self.assertEqual(queue.peek(), 1)
      self.assertEqual(queue.peek(), 1)
      self.assertEqual(queue.remove(), 1)
      self.assertEqual(queue.peek(), 2)
      self.assertEqual(queue.remove(), 2)


if __name__ == '__main__':
    unittest.main()
