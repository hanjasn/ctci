"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary
representation. If the number cannot be represented accurately in binary with at most 32 characters,
print "ERROR".
"""


class Solution:
  def to_binary_string(self, num: float) -> str:
    if not 0 < num < 1:
      return "ERROR"

    result = "0."
    while num > 0:
      if len(result) > 32:
        return "ERROR"
      
      num *= 2
      if num >= 1:
        result += "1"
        num -= 1
      else:
        result += "0"
    return result