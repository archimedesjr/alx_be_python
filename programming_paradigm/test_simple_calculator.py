import unittest
from simple_calculator.py import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

  def setUp(self):
    self.calc = SimpleCalculator()

  def test_addition(self):
    self.assertEqual(self.calc.add(5, 3), 8)

  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(8, 2), 6)

  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(8, 2), 16)
  
  def test_division(self):
    self.assertEqual(self.calc.divide(8, 2), 4)

if __name__ == "__main__":
  unittest.main()