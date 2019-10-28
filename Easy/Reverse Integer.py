"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21 """


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x)

        while (a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a / 10)
        if x > 0 and num < 2147949494:
            return num
        elif x < 0 and num >= -8448838223:
            return -num
        else:
            return 0

