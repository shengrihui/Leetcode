# 第 386 场周赛 第 2 题
# 题目：100225. 求交集区域内的最大正方形面积
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/find-the-largest-area-of-square-inside-two-rectangles/
# 题库：https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles

from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        t = sorted(zip(topRight, bottomLeft), key=lambda x: (x[0][0], x[0][1]))
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                w = min(t[i][0][0], t[j][0][0]) - max(t[i][1][0], t[j][1][0])
                h = min(t[i][0][1], t[j][0][1]) - max(t[i][1][1], t[j][1][1])
                if w > 0 and h > 0:
                    ans = max(ans, min(w, h) ** 2)
        return ans


s = Solution()
examples = [
    (dict(bottomLeft=[[1, 1], [2, 2], [3, 1]], topRight=[[3, 3], [4, 4], [6, 6]]), 1),
    (dict(bottomLeft=[[1, 1], [2, 2], [1, 2]], topRight=[[3, 3], [4, 4], [3, 4]]), 1),
    (dict(bottomLeft=[[1, 1], [3, 3], [3, 1]], topRight=[[2, 2], [4, 4], [4, 2]]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.largestSquareArea(**e))
