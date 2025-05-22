import unittest

class Solutions():
    def is_anagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False
    


class testSolution(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(Solutions.is_anagram(self, s="test", t="stet"))
        self.assertTrue(Solutions.is_anagram(self, s="test", t="tset"))
        self.assertTrue(Solutions.is_anagram(self, s="heystalker", t="hyestalkre"))


    def test_isnt_anagram(self):
        self.assertFalse(Solutions.is_anagram(self, s="notana", t="wrongans"))
    
    def test_empty(self):
        self.assertTrue(Solutions.is_anagram(self, s="", t=""))
        self.assertFalse(Solutions.is_anagram(self, s="", t="a"))
    
    def test_types(self):
        self.assertTrue(Solutions.is_anagram(self, s="123", t="321"))
        self.assertFalse(Solutions.is_anagram(self, s="123", t="456"))

        self.assertTrue(Solutions.is_anagram(self, s="!@#$%", t="%$#@!"))
        self.assertFalse(Solutions.is_anagram(self, s="!@#$%", t="^&*()"))







if __name__ == "__main__":
    unittest.main()