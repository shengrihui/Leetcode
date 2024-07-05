# 题目：100170. 对角线最长的矩形的面积
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-379/problems/maximum-area-of-longest-diagonal-rectangle/
# 题库：https://leetcode.cn/problems/maximum-area-of-longest-diagonal-rectangle
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d, ans = 0, 0
        for x, y in dimensions:
            r = x * x + y * y
            if r >= d:
                # 对角线一样取面积更大的
                # 对角线不一样直接算面积
                ans = x * y if r > d else max(ans, x * y)
                d = r
        return ans


# 灵神
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((x * x + y * y, x * y) for x, y in dimensions)[1]


s = Solution()
examples = [
    (dict(dimensions=[[9, 3], [8, 6]]), 48),
    (dict(dimensions=[[3, 4], [4, 3]]), 12),
    (dict(dimensions=[[6, 5], [8, 6], [2, 10], [8, 1], [9, 2], [3, 5], [3, 5]]), 20),
]
for e, a in examples:
    print(a, e)
    print(s.areaOfMaxDiagonal(**e))
