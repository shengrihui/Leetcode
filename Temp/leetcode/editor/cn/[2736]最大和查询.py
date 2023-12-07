# 2736 最大和查询
# leetcode submit region begin(Prohibit modification and deletion)
import typing
from typing import *


# class Solution:
#     def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
#         n, q = len(nums1), len(queries)
#         ans = [-1] * q
#         nums = sorted(zip(nums1, nums2), key=lambda x: -x[0])  # [nums1j,nums2j] 按 nums1j 降序排
#         j = 0
#         st = []  # [(nums2j , nums1j + nums2j )...]
#         for i, (x, y) in sorted(enumerate(queries), key=lambda x: -x[1][0]):  # [(idx,(x,y))..] 按 x 降序排序
#             while j < n and nums[j][0] >= x:  # 满足 nums1j<=x
#                 nums1j, nums2j = nums[j]
#                 # 什么情况入栈？
#                 # nums2j <= st[-1][0] ，无需加入
#                 # 因为 nums1j 是降序的，所以 nums2j + nums1j 也 <= st[-1][1]
#                 # 也就是让 nums2j(st[.][0]) 在栈中递增
#                 # 什么情况出栈？
#                 # 在入栈前，如果栈顶的 和(st[-1][1]) 比 nums1j + nums2j 小弹出
#                 # 因为 nums2j 比栈顶的大了，但对应的 nums1j 可能很小而导致 和 比较小，
#                 # 而这个时候如果查询的 y 标栈顶的 nums2j小，那这个查询的答案应当是栈顶的 和
#                 # 但如果新加入 nums1j + nums2j 更大（不低于） 栈顶的，
#                 # 那它肯定也更会是答案
#                 # 也就是让这个递减
#                 while st and st[-1][1] < nums1j + nums2j:
#                     st.pop()
#                 if not st or nums2j > st[-1][0]:
#                     st.append((nums2j, nums1j + nums2j))
#                 j += 1
#             p = bisect.bisect_left(st, (y,))  # 找到第一个大于等于 y 的位置，这之后的 st[.][0] 都满足
#             if p < len(st):
#                 ans[i] = st[p][1]
#         return ans
# class Solution:
#     def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
#         ans = [-1] * len(queries)
#         a = sorted(((a, b) for a, b in zip(nums1, nums2)), key=lambda p: -p[0])
#         j = 0
#         st = []
#         for i, (x, y) in sorted(enumerate(queries), key=lambda p: -p[1][0]):
#             while j < len(a) and a[j][0] >= x:  # 下面只需关心 ay (a[j][1])
#                 ax, ay = a[j]
#                 while st and st[-1][1] <= ax + ay:  # ay >= st[-1][0]
#                     st.pop()
#                 if not st or st[-1][0] < ay:
#                     st.append((ay, ax + ay))
#                 # print(st)
#                 j += 1
#             p = bisect_left(st, (y,))
#             print(p,st,y)
#             if p < len(st):
#                 ans[i] = st[p][1]
#         return ans
# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-sum-queries/solutions/2305395/pai-xu-dan-diao-zhan-shang-er-fen-by-end-of9h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


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
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums1), len(queries)
        ans = [-1] * q
        nums = sorted(zip(nums1, nums2), key=lambda x: -x[0])  # [nums1j,nums2j] 按 nums1j 降序排
        d = {v: i for i, v in
             enumerate(sorted(set(list(nums2) + [y for x, y in queries])))}  # 将 nums2 和 queries 中的值一起离散化
        m = len(d)
        seg = SegTree(lambda x, y: x if x > y else y, -1, m)
        idx = 0
        for i, (x, y) in sorted(enumerate(queries), key=lambda x: -x[1][0]):
            while idx < n and nums[idx][0] >= x:
                seg.set(d[nums[idx][1]], max(sum(nums[idx]), seg.get(d[nums[idx][1]])))
                idx += 1
            ans[i] = seg.prod(d[y], m)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
