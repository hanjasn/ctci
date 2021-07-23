"""
Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the
same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.

Example:
Input:  Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""


# Time: O(n)
# Space: O(n)
# Count number of times each letter appears in string and store result in hash table, and then check that at most one letter
# has an odd count.
class Solution:
  def palindrome_permutation(self, string: str) -> bool:
    if len(string) <= 2:
      return True
    
    lower_string = string.lower()
    freq_table = [0] * 26
    for c in lower_string:
      if ord('a') <= ord(c) <= ord('z'):
        freq_table[ord(c) - ord('a')] += 1
    
    odd_count = 0
    for f in freq_table:
      if f != 0 and f % 2 == 1:
        odd_count += 1
        if odd_count > 1:
          return False
    return True