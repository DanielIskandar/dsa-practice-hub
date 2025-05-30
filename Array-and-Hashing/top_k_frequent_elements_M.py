from typing import List
import unittest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements within the array.
        The test cases are generated such that the answer is always unique.
        You may return the output in any order.

        Example 1:
            Input: nums = [1,2,2,3,3,3], k = 2
            Output: [2,3]

        hash_set [#, occurences]
        """
        hash_set = []
        for num in nums:
            if num in hash_set:
                hash_set[num] += 1
            else:
                hash_set[num] = 1

        hash_set.sort()



class test_solution(unittest.TestCase):
    def test_function(self):
        nums = [1,2,2,3,3,3]
        k = 2
        correct_answer = [2,3]
        self.assertEqual(Solution.topKFrequent(self, nums, k), correct_answer)
