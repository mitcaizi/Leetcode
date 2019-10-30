"""Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    26 -> Z
    27 -> AA
    28 -> AB
Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"""

class Solution(object):
    def convertToTitle(self, n):
        result, num = "", n
        while num:
            result += chr((num - 1) % 26 + ord('A'))
            num = (num - 1) / 26
        return result[::-1]
if __name__ == "__main__":
    for i in range(1, 29):
        print(Solution().convertToTitle(i))

