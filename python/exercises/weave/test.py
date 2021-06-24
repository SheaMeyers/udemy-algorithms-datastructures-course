import unittest
from .main import Queue, weave


class TestWeave(unittest.TestCase):

    def test_queue(self):
      queue = Queue()
      queue.add(1)
      queue.add(2)
      self.assertEqual(queue.peek(), 1)
      self.assertEqual(queue.peek(), 1)
      self.assertEqual(queue.remove(), 1)
      self.assertEqual(queue.peek(), 2)
      self.assertEqual(queue.remove(), 2)
    
    def test_weave(self):
      one = Queue()
      one.add(1)
      one.add(2)
      one.add(3)
      one.add(4)

      two = Queue()
      two.add('one')
      two.add('two')
      two.add('three')
      two.add('four')

      result = weave(one, two)
      self.assertEqual(result.remove(), 1)
      self.assertEqual(result.remove(), 'one')
      self.assertEqual(result.remove(), 2)
      self.assertEqual(result.remove(), 'two')
      self.assertEqual(result.remove(), 3)
      self.assertEqual(result.remove(), 'three')
      self.assertEqual(result.remove(), 4)
      self.assertEqual(result.remove(), 'four')
      self.assertEqual(result.remove(), None)


if __name__ == '__main__':
    unittest.main()
