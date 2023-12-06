from typing import List
from collections import *
from itertools import *
from functools import *

# from math import *


# 题目：100126. 重新排列后包含指定子字符串的字符串数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-117/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/
# 题库：https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring

"""
# 所求方案数 = 随便字母，不受限制 - （重新排列后）不含有 leet
# # 随便字母，不受限制：
#    26 ** n
# # （重新排列后）不含有 leet
#   集合A：不含有 l
#   集合B：不含有 两个e => 至多含有一个 e => 没有 e 或者 有一个 e
#   集合C：不含有 t
#   容斥原理： |A| + |B| + |C| - |AB| - |BC| - |AC| + |ABC|
#   |A| = 不含有 l
#       = 25 ** n
#       = |C| = 25 * 25 ** (n-1)
#   |B| = 没有 e 或者 有一个 e
#       = 25 ** n + n * 25 ** (n-1)  # 先考虑那个 e 的位置可以有 n 种可能，剩下的 n-1 个位置25个字母任意
#   |A| + |B| + |C| = (25*2+25+n) * 25 ** (n-1) = (75+n) * 25 ** (n-1)
#   |AC| = 24 ** n
#   |AB| = 没有e或者有一个e 并且 没有t
#        = 没有e并且没有t  或者 有一个e但是没有t
#        = 24 ** n + n* 24**(n-1)
#        = |BC|
#   |AB| + |BC| + |AC| = 3 * 24**n + n * 24**(n-1)
#                      = 72 * 24**(n-1) + n * 24**(n-1)
#                      = (72+n*2) * 24**(n-1)
#   |ABC| = 没有l 并且 没有e或者有一个e 并且 没有t
#         = 没有l并且没有e并且没有t 或者 没有l并且有一个e并且没有t
#         = 23**n + n * 23**(n-1)
#         = (23+n) * 23**(n-1)

class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        return (pow(26, n, MOD)
                - pow(25, n - 1, MOD) * (75 + n)
                + pow(24, n - 1, MOD) * (72 + n * 2)
                - pow(23, n - 1, MOD) * (23 + n)) % MOD
"""


class Solution:
    def stringCount(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # 返回 i 个字母中至少 l个l ，e个e，t个t 的数量
        # 第 i 位选 l，由第 i-1 位 没有l，e个e，t个t 转移过来
        # 选 e和t 同理，
        # 其实都应该是 max(l/e/t-1,0)
        # 在 i=0 的时候，都没有字母了，只有三个参数都是0的时候才算是合法的，
        # 不然字母总数都是0了，l/e/t 怎么还能是非0呢？
        @cache
        def dfs(i: int, l: int, e: int, t: int) -> int:
            if i == 0:
                return l == e == t == 0
            return (dfs(i - 1, 0, e, t) +
                    dfs(i - 1, l, max(e - 1, 0), t) +
                    dfs(i - 1, l, e, 0) +
                    dfs(i - 1, l, e, t) * 23) % MOD

        return dfs(n, 1, 2, 1)


s = Solution()
examples = [
    (dict(n=3), 12),
    # (dict(n=10), 83943898),
]
for e, a in examples:
    print(a, e)
    print(s.stringCount(**e))
