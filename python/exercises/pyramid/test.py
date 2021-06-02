import unittest
import StringIO
import sys
from .main import pyramid


class TestSteps(unittest.TestCase):

    def test_steps_1(self):
      capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput

      pyramid(1)

      sys.stdout = sys.__stdout__
      self.assertEqual(
        capturedOutput.getvalue(), 
        '#\n'
      )

    def test_steps_2(self):
      capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput

      pyramid(2)

      sys.stdout = sys.__stdout__
      self.assertEqual(
        capturedOutput.getvalue(), 
        ' # \n###\n'
      )
    
    def test_steps_3(self):
      capturedOutput = StringIO.StringIO()
      sys.stdout = capturedOutput

      pyramid(3)

      sys.stdout = sys.__stdout__
      self.assertEqual(
        capturedOutput.getvalue(), 
        '  #  \n ### \n#####\n'
      )


if __name__ == '__main__':
    unittest.main()
