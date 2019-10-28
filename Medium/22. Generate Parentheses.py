"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        result = []
        self.a(n, n, '', result)
        return result
    def a(self, l, r, item, result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.a(l - 1, r, item + '(', result)
        if r > 0:
            self.a(l, r - 1, item + ')', result)
