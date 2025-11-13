import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()