# 131 分割回文串
# https://leetcode.cn/problems/palindrome-partitioning/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i: int) -> None:
            if i == n:
                nonlocal ans
                ans.append(path.copy())
                return
            for j in range(i, n):
                t = s[i:j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()

        ans = []
        path = []
        n = len(s)
        dfs(0)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
