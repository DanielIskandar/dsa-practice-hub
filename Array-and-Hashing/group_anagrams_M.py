from typing import List
import unittest
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

        Example 1:
            Input: strs = ["act","pots","tops","cat","stop","hat"]
            Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        ["act","pots","tops","cat","stop","hat"]
                                     ^
        s = "hat" sorted_s = "aht"


        output = [act: act, cat], [opst: pots, tops, stop], [aht, hat]
        """
        dict_set = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            # if sorted_str in dict_set:
                
            dict_set[sorted_str].append(s)
            # else:
            #     dict_set[sorted_str] = s
        return list(dict_set.values())




class Test_Solution(unittest.TestCase):
    def testRegular(self):
        input = ["act", "pots", "tops", "cat", "stop", "hat"]
        output = [["act", "cat"],["pots", "tops", "stop"],["hat"]]
        self.assertEqual(Solution.groupAnagrams(self, input), output)
        # self.assertAlmostEqual(Solution.groupAnagrams(self, input), output)


if "__main__" == __name__:
    unittest.main()