import unittest
from .main import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
      queue = Queue()
      queue.add(1)
      queue.add(2)
      queue.add(3)
      self.assertEqual(queue.remove(), 1)
      self.assertEqual(queue.remove(), 2)
      self.assertEqual(queue.remove(), 3)
      self.assertEqual(queue.remove(), None)


if __name__ == '__main__':
    unittest.main()
