from typing import List
import unittest

class Solution:
    """
    Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

    Please implement encode and decode

        Example 1:
            Input: ["neet","code","love","you"]
        
            '4#neet4#code4#love3#you'
             i^
            j^
            Output:["neet","code","love","you"]
    
        Example 2: 
            Input: ["we","say",":","yes"]

            Output: ["we","say",":","yes"]
    """

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""
        for s in strs:
            result += str(len(s))+ '#' + s
        return result

    def length_helper(self, i: int, s: str):
        s_length = ""
        while s[i] != '#':
            s_length += s[i]
            i += 1
        return int(s_length), i



    def decode(self, s: str) -> List[str]:
        i, j, count, result, s_length = 0, 0, 0, "", ""

        output = []
        while i < len(s) - 1:
            # while s[i] != '#':
            # str(s_length)
            # s_length = s[i]
            # i += 1
            s_length, i = self.length_helper(i, s)
            # while s[j] 
            j = i + 1
            s_length = int(s_length)
            count, result = 0, ""
            while count < s_length:
                result += s[j]
                j += 1
                count += 1
            output.append(result)
            i = j
        return output

class testSolution(unittest.TestCase):
    def test_function_regular(self):
        strs = ["neet","code","love","you"]
        self.assertEqual(Solution.decode(self, sol.encode(strs)), strs)
    
    def test_variational(self):
        strs = ["i", "don't", "really", "know", "whats", "going", "on", "ever"]
        self.assertEqual(Solution.decode(self, sol.encode(strs)), strs)
    
    def test_mixture_of_alnums(self):
        strs = ["6969", "420", "424909"]
        self.assertEqual(Solution.decode(self, sol.encode(strs)), strs)

    def test_long_word(self):
        strs = ["Antidisestablishmentarianism", "Hippopotomonstrosesquippedaliophobia", "hehelongwordsagagag"]
        self.assertEqual(Solution.decode(self, sol.encode(strs)), strs)





if __name__ == "__main__":
    strs = ["neet","code","love","you"]
    sol = Solution()
    sol.decode(sol.encode(strs))

    strs2 = ["Antidisest", "Hippopotomo", "hehelongwords"]
    sol2 = Solution()
    sol2.decode(sol2.encode(strs2))



    unittest.main()
    # Solution.twoSum([3,4,5,6], 7)

