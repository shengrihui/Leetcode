# 第 386 场周赛 第 2 题
# 题目：100225. 求交集区域内的最大正方形面积
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/find-the-largest-area-of-square-inside-two-rectangles/
# 题库：https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles

from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            topRight_xi, topRight_yi = topRight[i]
            bottomLeft_xi, bottomLeft_yi = bottomLeft[i]
            # 第 i 个不可能更大了
            if min(topRight_xi - bottomLeft_xi, topRight_yi - bottomLeft_yi) < ans:
                continue
            for j in range(i + 1, n):
                topRight_xj, topRight_yj = topRight[j]
                bottomLeft_xj, bottomLeft_yj = bottomLeft[j]
                w = (topRight_xj if topRight_xi > topRight_xj else topRight_xi) - (
                    bottomLeft_xi if bottomLeft_xi > bottomLeft_xj else bottomLeft_xj)
                h = (topRight_yi if topRight_yi < topRight_yj else topRight_yj) - (
                    bottomLeft_yi if bottomLeft_yi > bottomLeft_yj else bottomLeft_yj)
                if w > 0 and h > 0 and (mn := (w if w < h else h)) > ans:
                    ans = mn
        return ans ** 2


s = Solution()
examples = [
    (dict(bottomLeft=[[1, 1], [2, 2], [3, 1]], topRight=[[3, 3], [4, 4], [6, 6]]), 1),
    (dict(bottomLeft=[[1, 1], [2, 2], [1, 2]], topRight=[[3, 3], [4, 4], [3, 4]]), 1),
    (dict(bottomLeft=[[1, 1], [3, 3], [3, 1]], topRight=[[2, 2], [4, 4], [4, 2]]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.largestSquareArea(**e))
