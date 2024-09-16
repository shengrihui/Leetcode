# 第 415 场周赛 第 2 题
# 题目：100380. 最高乘法得分
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-415/problems/maximum-multiplication-score/
# 题库：https://leetcode.cn/problems/maximum-multiplication-score

from functools import *
from math import inf
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        tmp = [[aa * bb for bb in b] for aa in a]
        mn = -10 ** 10

        @cache
        def dfs(i: int, j: int) -> int:
            if j < 0:
                return mn
            if i == j:
                return sum(tmp[k][k] for k in range(i, -1, -1))
            res1 = dfs(i - 1, j)  # 不选
            r = dfs(i - 1, j - 1)
            res2 = (r if r != mn else 0) + tmp[j][i]  # 选
            return max(res1, res2)

        ans = dfs(n - 1, 3)
        dfs.cache_clear()
        return ans


# 记忆化搜索 0x3f
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if j < 0:
                return 0
            if i < 0:
                return -inf
            return max(dfs(i - 1, j), dfs(i - 1, j - 1) + a[j] * b[i])

        return dfs(len(b) - 1, 3)


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # n = len(b)
        # tmp = [[aa * bb for bb in b] for aa in a]
        # mn = -10 ** 10
        # f = [[mn] * n for _ in range(4)]
        # f[0][0] = tmp[0][0]
        # for i in range(1, n):
        #     f[0][i] = max(f[0][i - 1], tmp[0][i])
        # for j in range(1, 4):
        #     f[j][j] = tmp[j][j] + f[j - 1][j - 1]
        #     for i in range(j + 1, n - 3 + j):
        #         r1 = f[j][i - 1]
        #         r2 = f[j - 1][i - 1] + tmp[j][i]
        #         f[j][i] = max(r1, r2)
        # return f[-1][-1]
        n = len(b)
        f = [[-inf] * n for _ in range(4)]
        f[0][0] = a[0] * b[0]
        for i in range(1, n):
            f[0][i] = max(f[0][i - 1], a[0] * b[i])
        for j in range(1, 4):
            f[j][j] = a[j] * b[j] + f[j - 1][j - 1]
            for i in range(j + 1, n - 3 + j):
                r1 = f[j][i - 1]  # 第 j 个数不选 b[i]
                r2 = f[j - 1][i - 1] + a[j] * b[i]  # 第 j 个数选 b[i]
                f[j][i] = max(r1, r2)
        return f[-1][-1]


s = Solution()
examples = [
    (dict(a=[-7, 5, -10, -10], b=[7, -8, 8, -5, -5]), 196),
    (dict(a=[-7, 5, -10, -10], b=[7, -8, -1, 2, 4, 8, -5, -5, 5, -2, 4]), 196),
    (dict(a=[0, 10, 1, 1], b=[4, 0, 10, 7, 1, -9, -3, 7, -1, 8, 7, 1, 10, -7, -10, 7, 6]), 118),
    (dict(a=[3, 2, 5, 6], b=[2, -6, 4, -5, -3, 2, -7]), 26),
    (dict(a=[-1, 4, 5, -2], b=[-5, -1, -3, -2, -4]), -1),
]
for e, a in examples:
    print(a, e)
    print(s.maxScore(**e))
