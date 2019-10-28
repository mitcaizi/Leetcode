"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result