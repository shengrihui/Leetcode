# 第 411 场周赛 第 2 题
# 题目：100386. 超级饮料的最大强化能量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-411/problems/maximum-energy-boost-from-two-drinks/
# 题库：https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks

from functools import *
from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            # 第 i 个小时选 j 能量（j==0 A;j==1 B）
            # 如果这一次选 A，
            # 下一个从 A 选或挑一个选 B
            if i >= n:
                return 0
            x, y = energyDrinkA[i], energyDrinkB[i]
            res = 0
            if j == 0:
                res = max(res, x + dfs(i + 1, 0), x + dfs(i + 2, 1))
            if j == 1:
                res = max(res, y + dfs(i + 1, 1), y + dfs(i + 2, 0))
            return res

        n = len(energyDrinkA)
        res1 = dfs(0, 0)
        res2 = dfs(0, 1)
        return max(res2, res1)


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 1, j), dfs(i - 2, j ^ 1)) + c[j][i]

        n = len(energyDrinkA)
        c = [energyDrinkA, energyDrinkB]
        return max(dfs(n - 1, 0), dfs(n - 1, 1))


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        c = [energyDrinkA, energyDrinkB]
        # i = -2,-1,....n-1      n+2
        # j = 0,1
        f = [[0, 0] for _ in range(n + 2)]
        # dfs(-2,j) -> f[0][j]
        # dfs(-1,j) -> f[1][j]
        for i in range(n):
            for j in range(2):
                # dfs(i,j) = max(dfs(i - 1, j), dfs(i - 2, j ^ 1)) + c[j][i]
                f[i + 2][j] = max(f[i + 1][j], f[i][j ^ 1]) + c[j][i]
        return max(f[-1])


s = Solution()
examples = [
    (dict(energyDrinkA=[1, 3, 1], energyDrinkB=[3, 1, 1]), 5),
    (dict(energyDrinkA=[4, 1, 1], energyDrinkB=[1, 1, 3]), 7),
]
for e, a in examples:
    print(a, e)
    print(s.maxEnergyBoost(**e))
