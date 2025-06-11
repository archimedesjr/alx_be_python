import unittest
from simple_calculator.py import SimpleCalculator
class TestAdd(unittest.TestCase):

  def test_add(self):
    result = SimpleCalculator().add(5, 3)
    self.assertEqual(result, 8)

  def test_subtract(self):
    result = SimpleCalculator().subtract(8, 2)
    self.assertEqual(result, 6)

  def test_multiply(self):
    result = SimpleCalculator().multiply(8, 2)
    self.assertEqual(result, 16)
  
  def test_divide(self):
    result = SimpleCalculator().divide(8, 2)
    self.assertEqual(result, 4)
if __name__ == "__main__":
  unittest.main()