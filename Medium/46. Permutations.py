"""Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permute(n):
                answer.append([num] + y)
        return answer