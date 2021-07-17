"""
URLify

Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to
hold the additional characters and that you are given the "true" length of the string. (Note: If implementing in Java, please
use a character array so that you can perform this operation in place.)

Example:
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""

# Time: O(n)
# Space: O(n)
# Count spaces to find resulting length, and then loop backwards from original string and replace characters one by one from
# end of resulting string
class Solution:
  def urlify(self, s, length):
    s_list = list(s)
    num_spaces = 0
    for i in range(length):
      if s_list[i] == " ":
        num_spaces += 1
    new_length = length + num_spaces * 2
    for i in range(length - 1, -1, -1):
      if s_list[i] == " ":
        s_list[new_length - 1] = "0"
        s_list[new_length - 2] = "2"
        s_list[new_length - 3] = "%"
        new_length -= 3
      else:
        s_list[new_length - 1] = s_list[i]
        new_length -= 1
    return ''.join(s_list)