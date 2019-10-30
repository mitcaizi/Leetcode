"""Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12."""

class Solution:
    def rob(self, nums: List[int]) -> int:

        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
if __name__ == '__main__':
    print(Solution().rob([8, 4, 8, 5, 9, 6, 5, 4, 4, 10]))

