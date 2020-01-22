import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, factorial, None)
        self.assertRaises(TypeError, factorial, 1.0)
        self.assertRaises(TypeError, factorial, "")
        self.assertRaises(TypeError, factorial, ())
        self.assertRaises(TypeError, factorial, [])
        self.assertRaises(TypeError, factorial, {})

    def test_values(self):
        self.assertRaises(ValueError, factorial, -1)

    def test_success(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
