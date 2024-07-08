# 题目：100169. 移除栅栏得到的正方形田地的最大面积
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-377/problems/maximum-square-area-by-removing-fences-from-a-field/
# 题库：https://leetcode.cn/problems/maximum-square-area-by-removing-fences-from-a-field
from itertools import *
from typing import List

"""
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def helper(a: int, bar: List[int]) -> List[int]:
            bar.sort()
            bars = [1] + bar + [a]
            diff = []
            # 先求出两两相邻的
            for i, j in pairwise(bars):
                diff.append(j - i)
            arr = []
            # 每新取出一个 d 都加到上一个 d 加过的值上去
            for i, d in enumerate(diff):
                st = len(arr) - 1
                for j in range(i):
                    arr.append(arr[st - j] + d)
                arr.append(d)
            return arr

        vv = helper(n, vFences)
        hh = helper(m, hFences)
        hh = set(hh)
        for v in sorted(set(vv), reverse=True):
            if v in hh:
                return v * v % (10 ** 9 + 7)
        return -1
"""


# 用集合的方式
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def helper(a: int, bars: List[int]) -> set:
            bars.extend([1, a])
            bars.sort()
            # diff = set()
            # for i in range(len(bars)):
            #     for j in range(i + 1, len(bars)):
            #         diff.add(bars[j] - bars[i])
            # return diff
            return set(y - x for x, y in combinations(bars, 2))

        v = helper(n, vFences)
        h = helper(m, hFences)
        ans = max(v & h, default=0)
        return ans ** 2 % 1_000_000_007 if ans else -1


s = Solution()
examples = [
    (dict(m=4, n=3, hFences=[2, 3], vFences=[2]), 4),
    (dict(m=6, n=7, hFences=[2], vFences=[4]), -1),
    (dict(m=5, n=6, hFences=[4, 2, 3], vFences=[4, 5]), 16),
]
"""
5
6
[4,2,3]
[4,5]"""
for e, a in examples:
    print(a, e)
    print(s.maximizeSquareArea(**e))
