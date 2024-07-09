# 题目：100043. 购买物品的最大开销
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-117/problems/maximum-spending-after-buying-items/
# 题库：https://leetcode.cn/problems/maximum-spending-after-buying-items
from heapq import *
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        a = sorted([x for row in values for x in row])
        return sum(i * x for i, x in enumerate(a, 1))


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        h = [(values[i][-1], i, len(values[0]) - 1) for i in range(len(values))]
        heapify(h)
        d = 1
        ans = 0
        while h:
            v, i, j = heappop(h)
            ans += v * d
            d += 1
            if j > 0:
                heappush(h, (values[i][j - 1], i, j - 1))
        return ans


# 灵神的写法，pop 掉
"""
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        h = [(a[-1], i) for i, a in enumerate(values)]
        heapify(h)
        ans = 0
        for d in range(1, len(values) * len(values[0]) + 1):
            v, i = heappop(h)
            ans += v * d
            values[i].pop()
            if values[i]:
                heappush(h, (values[i][-1], i))
        return ans
"""

s = Solution()
examples = [
    (dict(values=[[8, 5, 2], [6, 4, 1], [9, 7, 3]]), 285),
    (dict(values=[[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]), 386),
]
for e, a in examples:
    print(a, e)
    print(s.maxSpending(**e))
