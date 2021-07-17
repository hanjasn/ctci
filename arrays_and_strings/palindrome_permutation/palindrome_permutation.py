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
# Assume case insensitive, whitespace insignificant, no punctuation
# Count number of times each letter appears in string and store result in hash table, and then check that at most one letter
# has an odd count.
class Solution:
  def palindrome_permutation(self, s):
    letters = self.count_letter_freq(s)
    return self.has_max_one_odd(letters)
  
  def count_letter_freq(self, s):
    arr = list(s.lower())
    letters = [0] * 26
    for c in arr:
      if ord('a') <= ord(c) <= ord('z'):
        letters[ord(c) - ord('a')] += 1
    return letters
  
  def has_max_one_odd(self, letters):
    count_odd = 0
    for count in letters:
      if count != 0 and count % 2 != 0:
        count_odd += 1
        if count_odd > 1:
          return False
    return True