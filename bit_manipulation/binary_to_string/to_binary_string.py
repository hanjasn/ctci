class Solution:
  def to_binary_string(self, num: float) -> str:
    return self.int_to_binary_string(int(num)//1) + "." + self.decimal_to_binary_string(num - num//1)
  
  def int_to_binary_string(self, num: int) -> str:
    if num == 0:
      return "0"
    
    result = ""
    while num > 0:
      result = str(num % 2) + result
      num //= 2
    return result
  
  def decimal_to_binary_string(self, num: float) -> str:
    if num == 0:
      return "0"
    
    result = ""
    while num > 0:
      if len(result) == 16:
        break
      
      num *= 2
      if num >= 1:
        result += "1"
        num -= 1
      else:
        result += "0"
    return result