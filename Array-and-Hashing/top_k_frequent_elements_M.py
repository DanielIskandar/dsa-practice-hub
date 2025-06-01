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
        hash_set = {}
        for num in nums:
            if num in hash_set:
                hash_set[num] += 1
            else:
                hash_set[num] = 1

        hash_list = list(hash_set.items())
        hash_list.sort(key=lambda pair: pair[1], reverse=False)
        sorted_keys = [key for key, value in hash_list]

        value_to_slice = len(hash_list) - k
        return sorted_keys[value_to_slice:]



class test_solution(unittest.TestCase):
    def test_function(self):
        nums = [1,2,2,3,3,3]
        k = 2
        correct_answer = [2,3]
        self.assertEqual(Solution.topKFrequent(self, nums, k), correct_answer)
    
    def test_out_of_order(self):
        nums = [3, 2, 1, 3, 2, 1, 3, 3, 2]
        k = 2
        correct_answer = [2, 3]
        self.assertEqual(Solution.topKFrequent(self, nums, k), correct_answer)
    
    def test_negative_values(self):
        nums = [-3, 2, 1, -3, 2, 1, -3, -3, 2]
        k = 2
        correct_answer = [2, -3]
        self.assertEqual(Solution.topKFrequent(self, nums, k), correct_answer)


if __name__ == "__main__":
    unittest.main()
