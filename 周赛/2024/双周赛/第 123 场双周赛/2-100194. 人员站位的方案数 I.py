# 第 123 场双周赛 第 2 题
# 题目：100194. 人员站位的方案数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-123/problems/find-the-number-of-ways-to-place-people-i/
# 题库：https://leetcode.cn/problems/find-the-number-of-ways-to-place-people-i
import bisect
from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt

# 三重循环，暴力直接超时
"""
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j: continue
                x2, y2 = points[j]
                if y2 <= y1 and x1 <= x2:
                    flag = True
                    for k in range(n):
                        if k == i or k == j: continue
                        a, b = points[k]
                        if x1 <= a <= x2 and y1 >= b >= y2:
                            flag = False
                            break
                    ans += flag
        return ans
"""
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        d = defaultdict(list)
        for x, y in points:
            d[y].append(x)
        for v in d.values():
            v.sort()
        y_list = sorted(d)
        for x, y in points:
            y_i = bisect.bisect_left(y_list, y)
            mx_x = inf
            for i in range(y_i, -1, -1):
                ny = y_list[i]
                big_x_i = bisect.bisect_left(d[ny], x)
                if big_x_i >= len(d[ny]):
                    continue
                big_x = d[ny][big_x_i]
                if i == y_i and big_x == x:
                    if big_x_i + 1 < len(d[ny]):
                        big_x = d[ny][big_x_i + 1]
                    else:
                        continue
                if big_x < mx_x:
                    ans += 1
                    mx_x = big_x
                if ny == y and big_x == x:
                    break
        return ans



s = Solution()
examples = [
    (dict(points=[[1, 4], [1, 1], [5, 4], [1, 0]]), 3),
    (dict(points=[[1, 1], [2, 2], [3, 3]]), 0),
    (dict(points=[[6, 2], [4, 4], [2, 6]]), 2),
    (dict(points=[[3, 1], [1, 3], [1, 1]]), 2),
    (dict(points=[[0, 1], [6, 1]]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfPairs(**e))
