import unittest

def square(number):
  """Returns the square of a numbers."""
  return number ** 3

class TestSquare(unittest.TestCase):

  def test_square(self):
    result = square(10)
    self.assertEqual(result, 100)

  def test_square_of_negative(self):
        self.assertEqual(square(-4), 16)

  def test_square_of_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == "__main__":
  unittest.main()