from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100127. 给小朋友们分糖果 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-117/problems/distribute-candies-among-children-ii/
# 题库：https://leetcode.cn/problems/distribute-candies-among-children-ii

# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         def f(m):  # 后面两个数和是m
#             if limit * 2 < m:  # 两个人都拿满了 limit 也不够 m，说明第一个人那多了，这个方案不行
#                 return 0
#             if limit >= m:  # 后面两个人每个人能拿的范围是 [0,m]，那两个人的和是 m 就有 m+1 种
#                 return m + 1
#             return limit - (m - limit) + 1  # 后面每个人的范围是 [0,limit]，但要和是 m，所以是 [m-limit,limit]
#
#         return sum(f(n - a) for a in range(min(limit, n) + 1))

# 所求方案数 = 所有分配方案 - 不合法方案数即有人的数量超过 limit
# # 所有分配方案：n 个糖果任意分给三个人
#   隔板法：C(n+2,2)
# # 不合法方案数即有人的数量超过 limit:
#   集合A、B、C分别表示甲乙丙三人分到的糖果数超过 limit 的方案数
#   容斥原理： |A| + |B| + |C| - |AB| - |BC| - |AC| + |ABC|
#   |A| = 甲分到的糖果数超过 limit 的方案数
#       = 甲已经分到了 limit 的糖果，剩下 n - limit 个糖果分给三个人且甲必须有一个方案数
#       = C(n-(limit+1)+2,2) = C(n-(limit+1)+2,2)
#   |B| = |C| = |A|
#   |AB| = C(n-2*(limit+1)+2,2)
#   |ABC| = C(n-3*(limit+1)+2,2)
def C2(n: int) -> int:  # 返回 C(n,2)
    return n * (n - 1) // 2 if n > 1 else 0  # 因为传入 n 可能会是负数


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return C2(n + 2) - 3 * C2(n - (limit + 1) + 2) + 3 * C2(n - 3 * (limit + 1) + 2) - C2(n - 2 * (limit + 1) + 2)


s = Solution()
examples = [
    (dict(n=5, limit=2), 3),
    (dict(n=3, limit=3), 10),
    (dict(n=1, limit=3), 3),
]
for e, a in examples:
    print(a, e)
    print(s.distributeCandies(**e))
