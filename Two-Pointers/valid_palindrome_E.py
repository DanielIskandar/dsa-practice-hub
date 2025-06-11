from typing import List
import unittest

class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, otherwise return false.

        A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

        Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

        Example 1:
            Input: s = "Was it a car or a cat I saw?"
            Output: true

            0    5             19      27
            Was it a car or a cat I saw?
                         ^       
                         ^
        """

        
        left, right = 0, len(s) - 1
        if len(s) < 2:
            return True
        while left < right:
            while s[left].isalnum() == False:
                if left < len(s) - 1:
                    left += 1
                else:
                    return True
            while s[right].isalnum() == False:
                if right > 0:
                    right -= 1
                else:
                    return True
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True



class testSolution(unittest.TestCase):
    def test_regular(self):
        input = "Was it a car or a cat I saw?"
        self.assertTrue(Solution.is_palindrome(self, input))

        input2 = "tab a cat"
        self.assertFalse(Solution.is_palindrome(self, input2))
    
    def test_spacing(self):
        input = "thisis s i s i h t"
        self.assertTrue(Solution.is_palindrome(self, input))

    def test_caps(self):
        input = "mom MOM"
        self.assertTrue(Solution.is_palindrome(self, input))

        input2 = "mom MOOM"
        self.assertFalse(Solution.is_palindrome(self, input2))
    
    def test_alnum(self):
        input = "12345 54321"
        self.assertTrue(Solution.is_palindrome(self, input))

        input2 = "!@mo$m mo$#@%m"
        self.assertTrue(Solution.is_palindrome(self, input2))

        input3 = "!@mo$m mo0o$#@%m"
        self.assertFalse(Solution.is_palindrome(self, input3))

    def test_empty(self):
        input2 = ""
        self.assertTrue(Solution.is_palindrome(self, input2))

        input = " "
        self.assertTrue(Solution.is_palindrome(self, input))
    
    def test_failed(self):
        input = ".,"
        self.assertTrue(Solution.is_palindrome(self, input))



if "__main__" == __name__:
    unittest.main()

