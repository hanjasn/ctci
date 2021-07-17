"""
One Away

There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

Example:
pale,  ple  -> true
pales, pale -> true
pale,  bale -> true
pale,  bake -> false
"""

# Time: O(n)
# Space: O(1)
# If the string lengths are equal, check for number of replacements needed. If the difference in string lengths is one, count
# the number of times each letter appears for each string separately in hash tables, and then count the number of letters that
# have different counts. If the differece in string lengths is greater than one, then return false.
class Solution:    
  def is_one_away(self, s1, s2):
    count_diff = 0
    if len(s1) == len(s2):
      for i in range(len(s1)):
        if s1[i] != s2[i]:
          count_diff += 1
          if count_diff > 1:
            return False
    elif abs(len(s1) - len(s2)) == 1:
      char_count_1, char_count_2 = [0] * 128, [0] * 128
      for char in s1:
        char_count_1[ord(char)] += 1
      for char in s2:
        char_count_2[ord(char)] += 1
      for i in range(128):
        if char_count_1[i] != char_count_2[i]:
          count_diff += 1
          if count_diff > 1:
            return False
    else:
      return False
    return True