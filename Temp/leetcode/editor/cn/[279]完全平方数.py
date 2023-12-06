# 279 完全平方数
from typing import *
from collections import *
from itertools import *
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


# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。 
# 
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4 
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁴ 
#  
# 
#  Related Topics 广度优先搜索 数学 动态规划 👍 1832 👎 0
