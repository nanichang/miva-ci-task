import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == '__main__':
    unittest.main()