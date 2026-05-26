"""
Generate (held in memory) Equation for natural #s between 1 & 100 that are divisible by 3 or 5

3 + 5 + 6 + 9 = 23

Unit tests

"""

from typing import List
def format_divisible_eq(start: int, end: int) -> str:
    # validate integers
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Both start and end must be ints")
    
    # validate bounds, inverted or empty
    if start < 1 or end < 1:
        raise ValueError("Start and end must be positive and non-zero")
    
    if start > end:
        raise ValueError("Inverted indexes are invalid")

    # Collect all #s of input
    # filter the range [start...end] for divisibiility by 3 or 5
    nums: List[int] = [i for i in range(start, end + 1) if i % 3 == 0 or i % 5 == 0]
    # 3 + 5 + 6 + 9 + 10 + 12 + 15 = sum

    # Compute sum
    total = sum(nums)

    # Building the equation
    # join the list of numbers as str use '+' and '= total'

    lhs = "+".join(str(n) for n in nums) # handles empty list -> ""

    if lhs == "": 
        # 0 = 0
        lhs = 0 

    return f"{lhs}={total}"



import unittest

class TestFormatDivisibleEq(unittest.TestCase):
    # empty or inverted ranges
    # start > end = 0
    # def test_empty_and_inverted(self):
    #     self.assertEqual(format_divisible_eq(10, 5), "=0")

    # Negatives and zero
    def test_negatives_and_zero(self):
        with self.assertRaises(ValueError):
            format_divisible_eq(0, 10)
        with self.assertRaises(ValueError):
            format_divisible_eq(-1, 10)
    
    def test_type_validation(self):
        with self.assertRaises(TypeError):
            format_divisible_eq(1.3, 10)
        with self.assertRaises(TypeError):
            format_divisible_eq("1", 10)


