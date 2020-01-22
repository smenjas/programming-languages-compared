import unittest
from euclid import euclid

class TestEuclid(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError, euclid, 1, None)
        self.assertRaises(TypeError, euclid, 1, 1.0)
        self.assertRaises(TypeError, euclid, 1, "")
        self.assertRaises(TypeError, euclid, 1, ())
        self.assertRaises(TypeError, euclid, 1, [])
        self.assertRaises(TypeError, euclid, 1, {})

    def test_values(self):
        self.assertRaises(ValueError, euclid, 1, 0)
        self.assertRaises(ValueError, euclid, 0, 1)
        self.assertRaises(ValueError, euclid, 1, -1)
        self.assertRaises(ValueError, euclid, -1, 1)

    def test_success(self):
        self.assertEqual(euclid(1, 1), 1)
        self.assertEqual(euclid(1, 2), 1)
        self.assertEqual(euclid(2, 2), 2)
        self.assertEqual(euclid(2, 3), 1)
        self.assertEqual(euclid(2, 4), 2)
        self.assertEqual(euclid(48, 64), 16)
