# 279 完全平方数
from collections import *
from functools import *
from math import *


# 递归
class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def dfs(i):
            sqr = isqrt(i)
            if sqrt(i) == sqr:
                return 1
            return min(dfs(i - x ** 2) + 1 for x in range(1, sqr + 1))

        return dfs(n)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            # for j in range(1, isqrt(n) + 1):
            #     dp[i] = min(dp[i], dp[i - j * j] + 1)
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


# leetcode submit region begin(Prohibit modification and deletion)
# BFS
class Solution:
    def numSquares(self, n: int) -> int:
        a = [i for i in range(isqrt(n), 0, -1)]
        q = deque()
        q.append((n, 0))
        while q:
            x, s = q.popleft()
            for i in a:
                nx = x - i * i
                if nx > 0:
                    q.append((nx, s + 1))
                elif nx == 0:
                    return s + 1
# leetcode submit region end(Prohibit modification and deletion)
