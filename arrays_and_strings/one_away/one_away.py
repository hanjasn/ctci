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
  def is_one_away(self, string1: str, string2: str) -> bool:
    length_diff = abs(len(string1) - len(string2))
    if length_diff > 1:
      return False

    count_diff = 0
    if length_diff == 1:
      freq_table_1 = [0] * 128
      freq_table_2 = [0] * 128
      for c in string1:
        freq_table_1[ord(c)] += 1
      for c in string2:
        freq_table_2[ord(c)] += 1
      for i in range(len(freq_table_1)):
        if freq_table_1[i] != freq_table_2[i]:
          count_diff += 1
          if count_diff > 1:
            return False
    else:
      for i in range(len(string1)):
        if string1[i] != string2[i]:
          count_diff += 1
          if count_diff > 1:
            return False
    return True