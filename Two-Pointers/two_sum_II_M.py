from typing import List
import unittest

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given an array of integers numbers that is sorted in non-decreasing order.

        - Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up 
        to a given target number target and index1 < index2. Note that index1 and index2 cannot 
        be equal, therefore you may not use the same element twice.

        - There will always be exactly one valid solution.

        - Your solution must use O(1) additional space.

        Example 1:

        Input: numbers = [1,2,3,4], target = 3
        Output: [1,2]
        """

        left, right = 0, len(numbers) - 1

        Solution.input_checker(self, numbers, target)

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    def input_checker(self, numbers: List[int], target):
        if not numbers or len(numbers) > 1000:
            raise ValueError("Number input size must be between 2 and 1000.")
        if target < -1000 and target > 1000:
            raise ValueError("Target input must be between -1000 and 1000 (inclusive)")
        

class testSolution(unittest.TestCase):
    def test_regular(self):
        numbers, target = [1,2,3,4], 3
        self.assertEqual(Solution.twoSum(self, numbers, target), [1,2])

        numbers2, target2 = [1,2], 3
        self.assertEqual(Solution.twoSum(self, numbers2, target2), [1,2])
    
    def test_duplicates(self):
        numbers, target = [1, 2, 2, 2, 3, 3, 3, 4], 7
        self.assertEqual(Solution.twoSum(self, numbers, target), [5,8])


    def test_empty(self):
        numbers, target = [], None
        # self.assertEqual(Solution.twoSum(self, numbers, target), [])
        with self.assertRaises(ValueError):
            Solution.twoSum(self, numbers, target)

if "__main__" == __name__:
    unittest.main()