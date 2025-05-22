from typing import List
import unittest

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
            Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

            Input: [1, 2, 2, 3, 4]
            Output: True

        """
        hashset = []
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.append(num)
        return False


class testSolution(unittest.TestCase):
    def testDuplicate(self):
        self.assertTrue(Solution.hasDuplicate(self, [1, 2, 2, 3, 4]))
    
    def testSinglet(self):
        self.assertFalse(Solution.hasDuplicate(self, [1, 2, 3, 4, 5]))

    def testAllDupes(self):
        self.assertTrue(Solution.hasDuplicate(self, [0, 0, 0, 0]))
    
    def testEmpty(self):
        self.assertFalse(Solution.hasDuplicate(self, [1]))
    
    def testNegatives(self):
        self.assertTrue(Solution.hasDuplicate(self, [-1, 1, -2, -5, -2, 3]))
        self.assertFalse(Solution.hasDuplicate(self, [-1, -2, -3, -4]))
    
    def testTypes(self):
        self.assertTrue(Solution.hasDuplicate(self, [1, 1.0]))
        self.assertFalse(Solution.hasDuplicate(self, [1, 1.4]))

if __name__ == '__main__':
    unittest.main()