import math
from functools import *
from itertools import *

# 题目：8028. 执行操作使两个字符串相等
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-366/problems/apply-operations-to-make-two-strings-equal/

# class Solution:
#     def minOperations(self, s1: str, s2: str, x: int) -> int:
#         diff = []
#         for i in range(len(s1)):
#             if s1[i] != s2[i]:
#                 diff.append(i)
#         n = len(diff)
#         # print(diff)
#         if n % 2:
#             return -1
#
#         # @cache
#         def dfs(ch, s):
#             nonlocal vis, ans
#             if ch == n:
#                 ans = min(ans, s)
#                 return
#             for i in range(n):
#                 for j in range(i + 1, n):
#                     if not vis[i] and not vis[j]:
#                         vis[i] = vis[j] = True
#                         dfs(ch + 2, s + min(diff[j] - diff[i], x))
#                         vis[i] = vis[j] = False
#
#         ans = float("inf")
#         vis = [False] * n
#         dfs(0, 0)
#         # for d in permutations(diff):
#         #     t = 0
#         #     for i in range(0, n, 2):
#         #         t += min(abs(d[i] - d[i + 1]), x)
#         #     ans = min(ans, t)
#         return ans


""""
先考虑什么时候是-1
因为无论是哪种操作，不会改变1的数量的奇偶性
因此，如果s1和s2的1的数量的奇偶性不一样，那就是-1了

从右往左想，
第i个字符可以的操作有：
1. 如果该位置一样且之前没有进行操作2，或者，进行了操作2但该位置本身不一样，直接进入下一个
2. 在之前没有进行操作2的情况下，执行操作2，或者操作1，并加上相应代价
3. 如果可以，免费操作一次

dfs(i,j,preRev)
i：当前判断的位置，
j：免费操作1的次数
preRev：上一个有没有进行操作2
"""


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        if s1.count("1") % 2 != s2.count("1") % 2:
            return -1

        @cache
        def dfs(i: int, j: int, preRev: bool) -> int:
            if j > i > 0:
                return math.inf
            if i < 0:
                # if j or preRev:  # 如果还能免费反转或者上一次进行了操作2，是不合法的
                #     return math.inf
                # return 0
                return math.inf if j or preRev else 0
            # if s1[i] == s2[i]:  # 如果该位置上两个一样，
            #     if not preRev:  # 且上一次没有进行操作2
            #         return dfs(i - 1, j, False)  # 带着一样的j直接进入下一个
            # else :  # 如果该位置上两个不一样
            #     if preRev:# 但上一次进行了操作2，也就是该位置上已经反转
            #         return dfs(i - 1, j, False)  # 也直接进入下一个
            # 以上简写成：
            if (s1[i] == s2[i]) == (not preRev):
                return dfs(i - 1, j, False)

            return min(dfs(i - 1, j, True) + 1,  # 采用操作2
                       dfs(i - 1, j - 1, False) if j > 0 else math.inf,  # 免费反转
                       dfs(i - 1, j + 1, False) + x,  # 采用操作1
                       )

        return dfs(len(s1) - 1, 0, False)


"""
不同的数量为奇数无法实现，因为不管哪种操作，都会改变偶数个字符。

p[]，不同字符（需要反转）的下标列表
dp[i]，完成到第i个字符的时候最小操作次数
dp[0] = x/2
dp[1] = min(dp[0] + x/2 ,p[1] - p[0])
      = min(x ,p[1] - p[0])
dp[2] = min(dp[1] + x/2 ,dp[0] + p[2] - p[1])
      = min(min(x ,p[1] - p[0]) + x/2 ,
             x/2 + p[2] - p[1])
      = min(min(x + x/2,p[1] - p[0] + x/2) ,
             x/2 + p[2] - p[1])
因为p长度一定是偶数，所以一定有dp[3]
dp[3] = min(dp[2] + x/2 ,dp[1] + p[3] - p[2])
      = min(min(min(x + x/2,p[1] - p[0] + x/2) ,x/2 + p[2] - p[1])+ x/2,
             min(x ,p[1] - p[0]) + p[3] - p[2])
      = min(min(min(2x,p[1] - p[0] + x) ,x + p[2] - p[1]),
             min(x ,p[1] - p[0]) + p[3] - p[2])
不写了，总之因为p的长度是偶数，所以最终一定dp[len(p)-1]的地方一定能有偶数个x/2，也就是能完整地进行操作1



"""


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        p = [i for i, (x, y) in enumerate(zip(s1, s2)) if x != y]
        m = len(p)
        if m == 0:
            return 0
        if m % 2:
            return -1
        # dp = [0] * m
        # dp[0] = x
        # dp[1] = min(dp[0] + x, 2 * (p[1] - p[0]))
        # for i in range(2, m):
        #     dp[i] = min(dp[i - 1] + x, dp[i - 2] + 2 * (p[i] - p[i - 1]))
        # return dp[-1] // 2
        f0, f1 = 0, x
        for i, j in pairwise(p):
            f0, f1 = f1, min(f1 + x, f0 + 2 * (j - i))
        return f1 // 2


s = Solution()
examples = [
    (dict(s1="1100011000", s2="0101001010", x=2), 4),
    (dict(s1="10110", s2="00011", x=4), -1),
    (dict(s1="01111101010100110100", s2="10010011011001011000", x=21), 7),
    (dict(s1="01111101010100110100",
          s2="10010011011001011000",
          x=21), 7),

]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
