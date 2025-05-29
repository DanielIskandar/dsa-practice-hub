from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

        You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

            Input: 
            nums = [3,4,5,6], target = 7

            Output: [0,1]

            [3,4,5,6]

            hash_set[index] = number

            get diff: (target - curr_num)
            check if diff is in hash set:
                if so return, current index(i) and hash_set[number]
            else:
                add hash_set[i] = num

            

            Constraints:
                2 <= nums.length <= 1000
                -10,000,000 <= nums[i] <= 10,000,000
                -10,000,000 <= target <= 10,000,000
        
        
        """

        prev_vals_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_vals_map:
                return [prev_vals_map[diff], i]
            prev_vals_map[num] = i # Must be set[num] because we search by key and we must find num
        
        print(prev_vals_map)

        """
        [3,4,5,6], target = 7
           ^
        diff = 7 - 4 = 3
        return(prev_vals_map[diff], i)

        prev_vals_map[0] = 3
        [0: 3]
        [1: ]
        []
        """



class testSolution(unittest.TestCase):
    def testValidSum(self):
        self.assertEqual(Solution.twoSum(self, [3,4,5,6], 7), [0,1])
        
    
    def testMultipleSums(self):
        self.assertEqual(Solution.twoSum(self, [1,2,3,4,5,6,7,8,9,10], 11), [4,5])
        # self.assertEqual(Solution.twoSum(self, [1,1,2,2], 3), [0,2]) <- BAD TEST CASE
    
    def testFailedCase(self):
        self.assertEqual(Solution.twoSum(self, [-1,-2,-3,-4,-5], -8), [2,4])
        # nums=[-1,-2,-3,-4,-5]
        # target=-8

if __name__ == "__main__":
    unittest.main()
    # Solution.twoSum([3,4,5,6], 7)

