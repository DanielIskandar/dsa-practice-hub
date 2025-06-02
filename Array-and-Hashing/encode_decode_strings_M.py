from typing import List
import unittest

class Solution:
    """
    Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

    Please implement encode and decode

        Example 1:
            Input: ["neet","code","love","you"]
                     ^
                     ... <- len(s)
                        ^
                         ,
            Output:["neet","code","love","you"]
    
        Example 2: 
            Input: ["we","say",":","yes"]

            Output: ["we","say",":","yes"]
    """

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""
        sizes = []
        for s in strs:
            sizes.append(len(s))

        for sz in sizes:
            result += str(sz)
            result += ','
        result += '#'
        # return result

        for s in strs:
            result += s

        return result



    def decode(self, s: str) -> List[str]:



# class testSolution(unittest.TestCase):


if __name__ == "__main__":
    strs = ["neet","code","love","you"]
    sol = Solution()
    sol.encode(strs)
    # unittest.main()
    # Solution.twoSum([3,4,5,6], 7)