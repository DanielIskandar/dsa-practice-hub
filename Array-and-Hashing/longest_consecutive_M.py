from typing import List
import unittest


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

        A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
        The elements do not have to be consecutive in the original array.

        You must write an algorithm that runs in O(n) time.
            Example 1:
            Input: nums = [2,20,4,10,3,4,5]
            Output: 4

            Example 2:
            Input: nums=[0,3,2,5,4,6,1,1]
            Output: 7
        """
        # Naive solution: Complexity O(N) + O(N log N)
        if not nums:
            return 0
        sorted_list = sorted(nums)
        consecutive, longest_seq = 0, 0
        for i in range(len(nums) - 1):
            difference = sorted_list[i + 1] - sorted_list[i]
            if difference == 1:
                consecutive += 1
                if consecutive > longest_seq:
                    longest_seq = consecutive
            elif difference < 1:
                continue
            else:
                consecutive = 0
        
        return longest_seq + 1
    
class Test_Solution(unittest.TestCase):
    def testRegular(self):
        nums = [2,20,4,10,3,4,5]
        self.assertEqual(Solution.longest_consecutive(self, nums), 4)
    
    def testLong(self):
        nums = [1, 10, 2, 14, 3, 16, 18, 4, 5, 6]
        self.assertEqual(Solution.longest_consecutive(self, nums), 6)
    
    def testNegative(self):
        nums = [-1, 10, -2, 14, -3, 16, 18, -4, -5, -6]
        self.assertEqual(Solution.longest_consecutive(self, nums), 6)
    
    def testFailed(self):
        nums=[0,3,2,5,4,6,1,1]
        self.assertEqual(Solution.longest_consecutive(self, nums), 7)
    
    def testEmpty(self):
        nums = []
        self.assertEqual(Solution.longest_consecutive(self, nums), 0)
    
if "__main__" == __name__:
    unittest.main()
