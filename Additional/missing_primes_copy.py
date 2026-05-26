"""
Write a function that inserts missing prime numbers for an input list of integers. 
For example, given the input of [1,2,6,7,8,12] the output would be [1,2,3,5,6,7,8,11,12].
"""
from typing import List

# Simple check of each value to see if  it is  prime
def is_prime(n: int) -> bool:
    # 0 and 1 are not prime values
    if n <= 1:
        return False
    
    # 2 and 3 are prime
    if n <= 3:
        return True
    
    # even numbers > 2 are bnot prime
    if n % 2 == 0:
        return False
    
    # test odd divisors only
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

def fill_missing_primes(nums: List[int]) -> List[int]:
    """
    1. Handle empty input list
    2. Sort & dedupe (remove duplicates) to process in order
    3. Iterate through adjacent pairs (previous, n)
        - For each integer between prev+1 and n-1, test with is_prime, then append
        - append n itself 
    
    """
    # empty list
    if not nums:
        return []
    
    nums = sorted(set(nums))
    result: List[int] = []

    prev = None

    for n in nums:
        # if first element -> add it
        if prev is None:
            result.append(n)
        else:
            # fill in primes between prev and n
            for candidate in range(prev + 1, n):
                if is_prime(candidate):
                    result.append(candidate)
            # append n itself (we are at the end of list)
            result.append(n)

        prev = n
    
    return result


import unittest

class TestFillMissingPrimes(unittest.TestCase):
    # empty list
    def test_empty(self):
        self.assertEqual(fill_missing_primes([]), [])
    
    # no missing primes
    def test_no_missing(self):
        self.assertEqual(fill_missing_primes([2, 3, 5]), [2, 3, 5])
    
    # test sorting, duplicates
    def test_unsorted_duplicates(self):
        self.assertEqual(fill_missing_primes([7, 2, 6, 2, 3]), [2, 3, 5, 6, 7])
    
    # single elements
    def test_single_elm(self):
        self.assertEqual(fill_missing_primes([4]), [4])


if __name__ == "__main__":
    unittest.main()
