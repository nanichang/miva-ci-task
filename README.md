# Code Crusaders Task
Automate Testing with GitHub Actions

__Objective:__ Set up a Continuous Integration (CI) pipeline using GitHub Actions to automatically run tests when code is pushed to the main branch.

__Sub-Task__
- __Team Leader:__ Design and configure the GitHub Actions workflow.
- __Members:__ Create unit tests for the project.
- __Members:__ Integrate the workflow with the tests and ensure proper triggers.



# Palindrome CI
<!--  -->
## Define Palindrome

A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as forward, ignoring spaces, punctuation, and capitalization. In other words, it is symmetrical and can be read identically from both directions.

### Requirements
- The program should take a string as input and return `True` if it is a palindrome, and `False` otherwise.

#### Examples of palindromes:

- Words: "madam", "racecar", "level"
- Numbers: 121, 12321

### Code Explanation

##### Step 1: Createing the Palindrome Python Program (palindrome.py)
```python
def is_palindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]
```
This function will check if the given string is a palindrome, ignoring case and non-alphanumeric characters. It first removes all non-alphanumeric characters and converts the string to lowercase. Then, it compares the original string with its reverse to determine if it is a palindrome.

##### Step 2: Test the Palindrome Program (test_palindrome.py)
```python
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
```

This code snippet defines a unit test class `TestPalindrome` that tests the `is_palindrome` function with various input strings. It uses the `unittest` module to run the test cases and check if the function correctly identifies palindromes.

##### Step 3: Run the Test
```
$ python test_palindrome.py
```

Running the test script will execute the test cases defined in the `TestPalindrome` class and output the results. If all tests pass, the function is correctly identifying palindromes.

##### Step 4: Set Up GitHub Actions Workflow (.github/workflows/palinedrome-ci.yml)
```yaml
name: Python Palindrome CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: python -m unittest discover

```
#### Committing and Deploying the Code
- Commit the changes to the repository.
- Push the changes to the main branch.
- Check the Actions tab in the GitHub repository to see the workflow running.
- Verify that the tests are executed successfully.
