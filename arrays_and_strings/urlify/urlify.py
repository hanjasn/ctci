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
  def urlify(self, string: str, length: int) -> str:
    space_count = 0
    for i in range(length):
      if string[i] == " ":
        space_count += 1
    
    new_length = length + space_count * 2
    string_arr = list(string)
    for i in range(length - 1, -1, -1):
      if string_arr[i] == " ":
        string_arr[new_length - 1] = "0"
        string_arr[new_length - 2] = "2"
        string_arr[new_length - 3] = "%"
        new_length -= 3
      else:
        string_arr[new_length - 1] = string_arr[i]
        new_length -= 1
    
    return ''.join(string_arr)