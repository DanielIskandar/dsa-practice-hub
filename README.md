# dsa-practice-hub
This is a way for me to practice my DSA skills with various mini-projects, leetcode problems, and coding challenges.
Figured this was a great way for me to track my progress!


### Problems Solved
|       Problem      | Topic | Difficulty | Language | Notes |
|--------------------|-------|------------|----------|-------|
| Contains Duplicate | Array |    Easy    |  Python  | Uses hash map |
| Is Anagram | Array |    Easy    |  Python  | Sorting string |
| Two Sum | Array | Easy | Python | Use a hash map (num, index). Check if diff(target - num) value encountered previously |
| Group Anagrams | Array | Medium | Python | Use an unordered dictionary. Make sure you return a list to avoid type errors |
| Top K Frequent Elements | Array | Medium | Python | Hashmap, values are the occurences. |
| Encode Decode Strings | Array | Medium | Python | Encode with [word][length]['#'] format. Decode with two pointer. Use helper function for double digit length words |
| Longest Consecutive Sequence | Array | Medium | Python | Use hashset. Check for beginning of sequence (num - 1) and continue to increment sequence and number until number is no longer in sequence. return max between current streak and longest sequence |
| Valid Palindrome | Two-Pointer | Easy | Python | Left and Right pointers, check with alnum and keep moving if not alnum. Don't forget to convert to lower case. |