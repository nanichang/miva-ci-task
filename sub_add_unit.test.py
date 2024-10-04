import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)
        self.assertEqual(-1 + 5, 4)
        self.assertEqual(0 + 0, 0)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
        self.assertEqual(-2 - 4, -6)
        self.assertEqual(7 - 7, 0)

if __name__ == '__main__':
    unittest.main()