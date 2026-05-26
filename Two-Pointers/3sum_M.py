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

        2 (3) pointer solution:

        [-4, -1, -1, 0, 1, 2]
              ^            
                           ^
        total: -1 + 0 + 1  = 0

        output: [-1, 0, 1], [-1, 0, 1]
        
        """
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    l += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            return res

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
    
    # def test_invalid_input(self):
    #     nums = [0,1]
    #     with self.assertRaises(ValueError):
    #         Solution.threeSum(self, nums)

    def test_duplicates(self):
        nums = [0,0,0,0]
        output = [[0,0,0]]
        self.assertEqual(Solution.threeSum(self, nums), output)

        nums2 = [-1,0,1,0]
        output2 = [[-1,1,0]]
        self.assertEqual(Solution.threeSum(self, nums2), output2)


if "__main__" == __name__:
    unittest.main()