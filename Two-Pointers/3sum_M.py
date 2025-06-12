import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and 
        the indices i, j and k are all distinct.

        - The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

        Example 1:
            Input: nums = [-1,0,1,2,-1,-4]
            Output: [[-1,-1,2],[-1,0,1]]
        
        Example 2:
            Input: nums = [0,1,1]
            Output: []
        
        Example 3:
            Input: nums = [0,0,0]
            Output: [[0,0,0]]

        Naive:
           \/
        [-1,0,1,2,-1,-4]
         ^            
              ^
        total: -1 + 0 + 1 = 0

        output: [-1, 2, -1], [-1, 0, 1]
        
        """
        output = []
        left, right = 0, len(nums) - 1

        Solution.input_validation(self, nums)

        while left < right:
            middle = left + 1 # Consider this might be a problem if the size of the array is 3 because you would just be checking right twice
            while middle < right:
                total_sum = nums[left] + nums[middle] + nums[right]
                if total_sum == 0 and [nums[left], nums[middle], nums[right]] not in output:
                    output.append([nums[left], nums[middle], nums[right]])
                    middle += 1 
                else:
                    middle += 1
            right -= 1
        return output

    def input_validation(self, nums: List[int]) -> List[List[int]]:
        """
        Constraints:
            3 <= nums.length <= 1000
            -10^5 <= nums[i] <= 10^5
        """
        if len(nums) < 3 or len(nums) > 1000:
            raise ValueError("Length of input list must be between 3 and 1000 (inclusive)")

class testSolution(unittest.TestCase):
    def test_regular(self):
        nums = [-1,0,1,2,-1,-4]
        output = [[-1,2,-1],[-1,0,1]]
        self.assertEqual(Solution.threeSum(self, nums), output)
    
    def test_small(self):
        nums = [0,1,1]
        output = []
        self.assertEqual(Solution.threeSum(self, nums), output)

        nums2 = [0,0,0]
        output2 = [[0,0,0]]
        self.assertEqual(Solution.threeSum(self, nums2), output2)
    
    def test_invalid_input(self):
        nums = [0,1]
        with self.assertRaises(ValueError):
            Solution.threeSum(self, nums)

    def test_failed_test(self):
        nums = [0,0,0,0]
        output = [[0,0,0]]
        self.assertEqual(Solution.threeSum(self, nums), output)


if "__main__" == __name__:
    unittest.main()