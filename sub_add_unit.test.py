import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 9, 10)

    def test_subtraction(self):
        self.assertEqual(5 - 4, 1)

if __name__ == '__main__':
    unittest.main()
