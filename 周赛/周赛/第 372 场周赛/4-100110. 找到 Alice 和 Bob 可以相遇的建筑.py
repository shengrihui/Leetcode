from typing import List
from collections import *
from itertools import *
from functools import *
from math import *

# 题目：100110. 找到 Alice 和 Bob 可以相遇的建筑
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-372/problems/find-building-where-alice-and-bob-can-meet/
# 题库：https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet

# 线段树

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

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        seg = SegTree(lambda x, y: x if x > y else y, 0, heights)
        n = len(heights)
        ans = []
        for a, b in queries:
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                ans.append(b)
            else:
                h = heights[a]
                l, r = b + 1, n  # [l,r)
                while l < r:
                    mid = (l + r) // 2
                    # [l,mid] => [l,mid+1) 内的最大值比 h 大
                    # 说明这一次询问要找的那个下标在这个范围里
                    if seg.prod(l, mid + 1) > h:
                        r = mid
                    else:
                        l = mid + 1
                ans.append(l if l != n else -1)
        return ans


# 单调栈
# 没成功
"""
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        suf = [n] * n
        st = [n]
        for i in range(n):
            h = heights[-i - 1]
            while len(st) > 1 and heights[st[-1]] <= h:
                st.pop()
            suf[-i - 1] = st[-1]
            st.append(n - i - 1)
        print(heights)
        print(suf)

        ans = []
        for q in queries:
            q.sort()
            a, b = q
            if heights[b] > heights[a] or a == b:
                ans.append(b)
            else:
                # heights[a] > heights[b]
                while True:
                    a = suf[a]
                    if a == n:
                        ans.append(-1)
                        break
                    if a > b:
                        ans.append(a)
                        break
        return ans
"""

# 暴力 + 一点点自以为是的优化
# 超时
"""
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        ans = [-1] * len(queries)
        for q in queries:
            if q[0] > q[1]:
                q[1], q[0] = q
        sb = -1
        d = dict()
        for i, (a, b) in sorted(enumerate(queries), key=lambda iq: (iq[1][1], heights[iq[1][0]])):
            if heights[b] > heights[a] or a == b:
                ans[i] = b
            else:
                if b != sb:
                    sb = b
                ga = d.get(a, 0)
                if ga > b:
                    ans[i] = ga
                    sb = ga
                    continue
                while sb < n:
                    if heights[sb] > heights[a]:
                        ans[i] = sb
                        d[a] = sb
                        break
                    sb += 1
        return ans
"""

s = Solution()
examples = [
    (dict(heights=[6, 4, 8, 5, 2, 7], queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]), [2, 5, -1, 5, 2]),
    (dict(heights=[5, 3, 8, 2, 6, 1, 4, 6], queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]), [7, 6, -1, 4, 6]),
]
for e, a in examples:
    print(a, e)
    print(s.leftmostBuildingQueries(**e))
