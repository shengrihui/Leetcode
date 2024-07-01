# 第 404 场周赛 第 1 题
# 题目：100340. 三角形的最大高度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-404/problems/maximum-height-of-a-triangle/
# 题库：https://leetcode.cn/problems/maximum-height-of-a-triangle

from itertools import *


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def f(a, b):
            for i in count(1):
                if i % 2:
                    a -= i
                else:
                    b -= i
                if a < 0 or b < 0:
                    return i - 1

        return max(f(red, blue), f(blue, red))


s = Solution()
examples = [
    (dict(red=2, blue=4), 3),
    (dict(red=2, blue=1), 2),
    (dict(red=1, blue=1), 1),
    (dict(red=10, blue=1), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maxHeightOfTriangle(**e))
