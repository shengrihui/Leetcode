# 题目：100133. 购买水果需要的最少金币数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-118/problems/minimum-number-of-coins-for-fruits/
# 题库：https://leetcode.cn/problems/minimum-number-of-coins-for-fruits
from collections import deque
from functools import *
from math import *
from typing import List

"""
题目说下标从 1 开始，为了方便和统一，在前面加一个 0
这样，最后一个水果的下标是 n

定义：dfs(i) 表示获得 [i,n] 的水果需要的最少金币，而且 i 要花钱买

转移：dfs(i) = price[i] + min{dfs(j)} 
       i+1 <= j <= 2i+1
       因为 i 花钱了最多可以免费到 i+i，2i+1 必须要花钱了
       也就是说，花钱卖了 i 之后，再要获得之后所有水果的最小花费，
       就考虑下一个要花钱的 j
       j 的上界还可以和 n 取较小值

出口：
    i > n return 0 已经获得所有水果
    2i+1 > n return prices[i] 后面水果都可以获得了

入口：dfs(1) 即答案
"""


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


# 转成递推
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        prices = [0] + prices
        for i in range((n - 1) // 2, 0, -1):
            prices[i] += min(prices[i + 1:i + i + 2])
        return prices[1]


# 线段树
# 区间查询 min(prices[i + 1:i + i + 2])
"""
import typing


class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        prices = [0] + prices
        seg = SegTree(lambda x, y: x if x < y else y, inf, prices)
        for i in range(n // 2 - (n % 2 == 0), 0, -1):
            seg.set(i, prices[i] + seg.prod(i + 1, i + i + 2))
        return seg.get(1)
"""


# 单调队列
# 灵神代码
# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/solutions/2542044/dpcong-on2-dao-onpythonjavacgo-by-endles-nux5
# 从队首到队尾的下标值是变大的，因此第一个循环从队尾 pop
# 从队首到队尾的 price 值是变大的，且第一个值最小，因此第一个循环从队尾 pop
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        q = deque([(n + 1, 0)])  # 哨兵
        for i in range(n, 0, -1):
            while q[-1][0] > i * 2 + 1:  # 右边离开窗口
                q.pop()
            f = prices[i - 1] + q[-1][1]
            while f <= q[0][1]:
                q.popleft()
            q.appendleft((i, f))  # 左边进入窗口
        return q[0][1]


s = Solution()
examples = [
    (dict(prices=[3, 1, 2]), 4),
    (dict(prices=[1, 10, 1, 1]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCoins(**e))
