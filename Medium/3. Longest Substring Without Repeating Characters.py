"""Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = -1
        max = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i - start > max:
                    max = i - start
        return max
    if __name__ == '__main__':
        print(Solution().lengthOfLongestSubstring('pwwkew'))