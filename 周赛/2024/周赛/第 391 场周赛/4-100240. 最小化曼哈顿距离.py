# 第 391 场周赛 第 4 题
# 题目：100240. 最小化曼哈顿距离
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-391/problems/minimize-manhattan-distances/
# 题库：https://leetcode.cn/problems/minimize-manhattan-distances

from math import inf
from typing import List

# https://leetcode.cn/problems/minimize-manhattan-distances/solutions/2716755/tu-jie-man-ha-dun-ju-chi-heng-deng-shi-b-op84
from sortedcontainers import SortedList


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        xs = SortedList()
        ys = SortedList()
        for x, y in points:
            xs.add(x + y)
            ys.add(y - x)
        ans = inf
        for x, y in points:
            x, y = x + y, y - x
            xs.remove(x)
            ys.remove(y)
            ans = min(ans, max(xs[-1] - xs[0], ys[-1] - ys[0]))
            xs.add(x)
            ys.add(y)
        return ans
