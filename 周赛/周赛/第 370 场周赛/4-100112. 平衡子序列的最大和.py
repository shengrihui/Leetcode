from math import *
from typing import List

# 题目：100112. 平衡子序列的最大和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-370/problems/maximum-balanced-subsequence-sum/
# 题库：https://leetcode.cn/problems/maximum-balanced-subsequence-sum/description/

# 比赛时朴素dfs  ###################################################
"""
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        need_vis = [x > 0 for x in nums]

        @cache
        def dfs(start):
            nonlocal need_vis
            if start == n - 1:
                return nums[-1]
            x = nums[start]
            res = x
            for i in range(start + 1, n):
                if need_vis[i] and nums[i] - nums[start] >= i - start:
                    res = max(res, x + dfs(i))
            return res

        ans = dfs(0)
        for i in range(1, n):
            ans = max(ans, dfs(i))
        return ans
"""

# 有序列表 #########################################################
"""
from sortedcontainers import SortedList


class Node:
    def __init__(self, x, s, idx):
        self.x = x
        self.s = s
        self.idx = idx

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.s > other.s


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        sl = SortedList()
        le0 = -inf  # less equal 0
        for i, x in enumerate(nums):
            if x <= 0:
                le0 = x if x > le0 else le0
                continue
            l, r = 0, len(sl) - 1
            while l <= r:
                mid = (l + r) // 2
                if sl[mid].x < x:
                    l = mid + 1
                else:
                    r = mid - 1
            while True:
                if r == -1:
                    sl.add(Node(x, 0 + x, i))
                    break
                if x - sl[r].x >= i - sl[r].idx:
                    sl.add(Node(x, sl[r].s + x, i))
                r -= 1
        return max(sl).s if sl else le0
"""

# 小羊肖恩线段树 ####################################################
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
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        b = sorted(v - i for i, v in enumerate(nums))
        d = {v: i for i, v in enumerate(b)}
        seg = SegTree(lambda x, y: x if x > y else y, -inf, len(b))
        for i, x in enumerate(nums):
            fi = d[x - i]
            pre_max = seg.prod(0, fi + 1)  # 因为非降，所以可以邓毅f[fi]
            seg.set(fi, x + (pre_max if pre_max > 0 else 0))
        return seg.all_prod()


s = Solution()
examples = [
    (dict(nums=[3, 3, 5, 6]), 14),
    (dict(nums=[5, -1, -3, 8]), 13),
    (dict(nums=[-2, -1]), -1),
    (dict(nums=[4, -1, 5, -1, -7]), 5),
    (dict(nums=[-9, 11, 5, 22, 44, -20, 13, 19, 9, -29, -47, 43, -7, -42, 41, 18, 19, -19]), 80),
    (dict(nums=[575620823, 479033595, 886887886, -852474608, -420672886, 737934355, 250403064, 224283339, -384976809,
                -987461626, 136509483, -129866226, -50565237, -154338484, 371077418, 272664294, -814150532, 282117543,
                -674366550, 980489639, 478540645, 524203028, 441371360, 931402588, 631069517, -440061776, -349919062,
                -997020816, -673216767, -967823902, -147997697, 657232417, -494078349, -992757880, -266413795,
                -777674117, 368378534, -375023270, -254102878, 622258046, 812136726, 129723835, 385726066, 967687286,
                413321239, 893607725, -418185339, 969104215, -210035992, 106222252, -780639712, -453627658, 408765,
                73492241, 134247969, -43313029, 458832315, -733286392, 830315216, -46271051, -409056279, 371769566,
                -377983919, -684016074, 191191576, 155393414, 688854167, -862076015, 85180768, -243038107, 743938595,
                -342865814, 292132080, -714507316, 147251588, 94112383, -358927530, 700323565, -368012981, 197539072,
                708268772, 254071579, 606822947, -489399226, -679189244, 665305192, -769036220, 430483104, -318526174,
                414100547, -297904159, 480799012, -735010777, 108672899, 700609431, -161130210, 869362253, -704822568,
                216612973, -260100677, -721625345, 278757454, -584467200, -883426202, 550827022, 467127468, 593877505,
                -881835983, -173050545, -364289198, 36917255, 527300781, 176637416, -936500748, 220839201, -529943007,
                699610346, 490713426, -597641135, 12258605, -817658657, 898907036, -908524193, -275203042, -87568409,
                717950938, 984379061, 280574937, 862009093, 582974077, -323812156, 176370, -292822669, -160968769,
                503188602, -914880597, -750451047, -304156511, -398869607, 272163701, -927180124, 352367475, 25473538,
                -385461217, 744034846, -979839284, 655013553, 324567817, -556275677, 731850874, -191777741, 351705580,
                205443907, 742400276, -174827408, 752240530, -953151888, -477679296, 428916743, 780568367, 805817853,
                -764514879, 923422290, -705001082, -594889405, -584548133, -789549180, 746549311, -906594869, 552042120,
                409194293, 867152288]), 80),
]
for e, a in examples:
    print(a, e)
    print(s.maxBalancedSubsequenceSum(**e))
    # break
