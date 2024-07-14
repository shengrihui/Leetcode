# 17 电话号码的字母组合
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
mp = {"2": "abc",
      "3": "def",
      "4": "ghi",
      "5": "jkl",
      "6": "mno",
      "7": "pqrs",
      "8": "tuv",
      "9": "wxyz"}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i: int) -> None:
            if i == len(digits):
                nonlocal ans
                ans.append("".join(path))
                return
            for c in mp[digits[i]]:
                path.append(c)
                dfs(i + 1)
                path.pop()

        path = []
        ans = []
        if not digits:
            return ans
        dfs(0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
