"""
String Compression

Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
"""


# Time: O(n)
# Space: O(n)
# Add characters to array first, then convert to string at end
class Solution1:
    def compress_string(self, s: str) -> str:
        length = 0
        for i in range(1, len(s) + 1):
            if i == len(s) or s[i] != s[i - 1]:
                length += 2
        if length >= len(s):
            return s

        result = []
        count = 0
        for i in range(1, len(s) + 1):
            count += 1
            if i == len(s) or s[i] != s[i - 1]:
                result.append(s[i - 1] + str(count))
                count = 0
        return ''.join(result)


# Time: O(n^2) due to string concatenation
# Space: O(n)
class Solution2:
    def compress_string(self, s: str) -> str:
        result = ""
        count = 0
        for i in range(1, len(s) + 1):
            count += 1
            if i == len(s) or s[i] != s[i - 1]:
                result += s[i - 1] + str(count)
                count = 0
        
        return result if len(result) < len(s) else s