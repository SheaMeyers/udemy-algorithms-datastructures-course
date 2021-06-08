import unittest
from .main import fib


class TestFib(unittest.TestCase):

    def test_1(self):
      self.assertEqual(fib(1), 1)

    def test_2(self):
      self.assertEqual(fib(2), 1)

    def test_3(self):
      self.assertEqual(fib(3), 2)

    def test_4(self):
      self.assertEqual(fib(4), 3)

    def test_39(self):
      self.assertEqual(fib(39), 63245986)


if __name__ == '__main__':
    unittest.main()
