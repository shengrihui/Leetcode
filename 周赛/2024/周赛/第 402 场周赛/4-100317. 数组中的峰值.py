# 第 402 场周赛 第 4 题
# 题目：100317. 数组中的峰值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-402/problems/peaks-in-array/
# 题库：https://leetcode.cn/problems/peaks-in-array

import typing
from typing import List


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
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        vv = [0] * n
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                vv[i] = 1
        seg = SegTree(lambda x, y: x + y, 0, vv)
        ans = []
        for q, a, b in queries:
            if q == 1:
                if b == a + 1 or a == b:
                    ans.append(0)
                else:
                    ans.append(seg.prod(a + 1, b))
            elif q == 2:
                nums[a] = b
                left, right = a - 1, a + 1

                def f(idx):
                    if nums[idx] > nums[idx + 1] and nums[idx] > nums[idx - 1]:
                        seg.set(idx, 1)
                    else:
                        seg.set(idx, 0)

                if 0 < a < n - 1:
                    f(a)
                if 1 < a:
                    f(left)
                if a < n - 2:
                    # print(a,right)
                    f(right)
        return ans


s = Solution()
examples = [
    (dict(nums=[4, 9, 4, 10, 7], queries=[[2, 3, 2], [2, 1, 3], [1, 2, 3]]), [0]),
    (dict(nums=[3, 6, 9], queries=[[1, 1, 1], [1, 2, 2], [2, 2, 3]]), [0, 0]),
    (dict(nums=[4, 5, 5], queries=[[1, 2, 2], [1, 0, 1], [1, 1, 2]]), [0, 0, 0]),
    (dict(nums=[3, 1, 4, 2, 5], queries=[[2, 3, 4], [1, 0, 4]]), [0]),
    (dict(nums=[4, 1, 4, 2, 1, 5], queries=[[2, 2, 4], [1, 0, 2], [1, 0, 4]]), [0, 1]),
]
for e, a in examples:
    print(a, e)
    print(s.countOfPeaks(**e))
