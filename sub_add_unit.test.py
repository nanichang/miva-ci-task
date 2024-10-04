import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()