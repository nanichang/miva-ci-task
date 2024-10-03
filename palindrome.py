def is_palindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]