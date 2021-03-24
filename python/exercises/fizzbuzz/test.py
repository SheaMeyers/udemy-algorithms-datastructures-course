import unittest
import StringIO
import sys
from .main import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
      capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput

      fizz_buzz(15)

      sys.stdout = sys.__stdout__
      self.assertEqual(
        capturedOutput.getvalue(), 
        '1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n'
      )


if __name__ == '__main__':
    unittest.main()
