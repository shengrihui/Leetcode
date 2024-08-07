# 1671 得到山形数组的最少删除次数
# https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/


# leetcode submit region begin(Prohibit modification and deletion)
# 前后缀分解 + 最长递增子序列
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        a = []
        for i, x in enumerate(nums):
            p = bisect.bisect_left(a, x)
            if p == len(a):
                a.append(x)
            a[p] = x
            pre[i] = p + 1

        a = []
        ans = 0
        for i in range(n - 1, 0, -1):
            x = nums[i]
            p = bisect.bisect_left(a, x)
            if len(a) == p:
                a.append(x)
            a[p] = x
            if pre[i] >= 2 and p >= 1:  # 山顶两边都要有数字
                # nums[i]左边的最长递增子序列长度pre[i]（包括nums[i]）+ nums[i]右边的最长递增子序列长度（不包括nums[i]）p
                ans = max(ans, pre[i] + p)
        return n - ans


# leetcode submit region end(Prohibit modification and deletion)

# 测试用例
"""
[9,8,1,7,6,5,4,3,2,1]
[100,92,89,77,74,66,64,66,64]
"""
# 线段树
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
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        d = {v: i for i, v in enumerate(sorted(set(nums)))}
        m = len(d) + 1

        seg = SegTree(lambda x, y: x if x > y else y, -1, m)
        left = [0] * n
        for i, x in enumerate(nums):
            c = seg.prod(0, d[x])
            seg.set(d[x], c + 1)
            left[i] = c + 1

        seg = SegTree(lambda x, y: x if x > y else y, -1, m)
        ans_ = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            c = seg.prod(0, d[x])
            seg.set(d[x], c + 1)
            if c + 1 > 0 and left[i] > 0:
                ans_ = max(ans_, c + 1 + left[i] + 1)
        return n - ans_
"""
