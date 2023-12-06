from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100133. 购买水果需要的最少金币数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-118/problems/minimum-number-of-coins-for-fruits/
# 题库：https://leetcode.cn/problems/minimum-number-of-coins-for-fruits
# import typing
#
#
# class SegTree:
#     def __init__(self,
#                  op: typing.Callable[[typing.Any, typing.Any], typing.Any],
#                  e: typing.Any,
#                  v: typing.Union[int, typing.List[typing.Any]]) -> None:
#         self._op = op
#         self._e = e
#
#         if isinstance(v, int):
#             v = [e] * v
#
#         self._n = len(v)
#         self._log = (self._n - 1).bit_length()
#         self._size = 1 << self._log
#         self._d = [e] * (2 * self._size)
#
#         for i in range(self._n):
#             self._d[self._size + i] = v[i]
#         for i in range(self._size - 1, 0, -1):
#             self._update(i)
#
#     def set(self, p: int, x: typing.Any) -> None:
#         assert 0 <= p < self._n
#
#         p += self._size
#         self._d[p] = x
#         for i in range(1, self._log + 1):
#             self._update(p >> i)
#
#     def get(self, p: int) -> typing.Any:
#         assert 0 <= p < self._n
#
#         return self._d[p + self._size]
#
#     def prod(self, left: int, right: int) -> typing.Any:
#         assert 0 <= left <= right <= self._n
#         sml = self._e
#         smr = self._e
#         left += self._size
#         right += self._size
#
#         while left < right:
#             if left & 1:
#                 sml = self._op(sml, self._d[left])
#                 left += 1
#             if right & 1:
#                 right -= 1
#                 smr = self._op(self._d[right], smr)
#             left >>= 1
#             right >>= 1
#
#         return self._op(sml, smr)
#
#     def _update(self, k: int) -> None:
#         self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])
#
#
# class Solution:
#     def minimumCoins(self, prices: List[int]) -> int:
#         n = len(prices)
#         prices = [0] + prices
#         seg = SegTree(lambda x, y: x if x < y else y, inf, prices)
#         for i in range(n // 2 - (n % 2 == 0), 0, -1):
#             seg.set(i, prices[i] + seg.prod(i + 1, i + i + 2))
#         return seg.get(1)


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i > n:
                return 0
            if i * 2 + 1 > n:
                return prices[i]
            res = inf
            for j in range(i + 1, min(i + i + 2, n + 2)):
                res = min(res, dfs(j))
            return prices[i] + res

        n = len(prices)
        prices = [0] + prices
        return dfs(1)


s = Solution()
examples = [
    (dict(prices=[3, 1, 2]), 4),
    (dict(prices=[1, 10, 1, 1]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCoins(**e))
