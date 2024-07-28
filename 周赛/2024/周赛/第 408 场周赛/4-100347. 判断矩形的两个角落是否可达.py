# 第 408 场周赛 第 4 题
# 题目：100347. 判断矩形的两个角落是否可达
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-408/problems/check-if-the-rectangle-corner-is-reachable/
# 题库：https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable

from typing import List

# 方法一
# 连通块的范围会不会挡住从原点到右上角的路
"""
from collections import defaultdict
class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        p = list(range(n))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i, (x, y, r) in enumerate(circles):
            for j in range(i):
                xx, yy, rr = circles[j]
                if hypot(x - xx, y - yy) <= r + rr:
                    pi, pj = find(i), find(j)
                    if pi != pj:
                        p[pi] = pj

        st = defaultdict(list)
        for i in range(n):
            st[find(i)].append(i)
        # print(st.values())
        for tmp in st.values():
            left, right, up, down = inf, 0, 0, inf
            for i in tmp:
                x, y, r = circles[i]
                left = min(left, x - r)
                right = max(right, x + r)
                if left <= 0 and right >= X:
                    return False
                down = min(down, y - r)
                up = max(up, y + r)
                if down <= 0 and up >= Y:
                    return False
                if up >= Y and right >= X or down <= 0 and left <= 0:
                    return False
        return True
"""


# 方法二
# 上边和左边作为 n，下边和右边作为 n+1
# 如果 n 和 n=1 在一个连通块里，return False
class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        p = list(range(n + 2))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def merge(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                p[pi] = pj

        for i, (x, y, r) in enumerate(circles):
            if x - r <= 0 or y + r >= Y:
                merge(i, n)
            if x + r >= X or y - r <= 0:
                merge(i, n + 1)
            for j in range(i):
                xx, yy, rr = circles[j]
                if (x - xx) ** 2 + (y - yy) ** 2 <= (r + rr) ** 2:
                    merge(i, j)
            if find(n) == find(n + 1):
                return False
        return True


s = Solution()
examples = [
    # (dict(X=3, Y=3, circles=[[2, 4, 1], [4, 4, 1], [4, 2, 1]]), True),
    # (dict(X=3, Y=3, circles=[[2, 1000, 997], [1000, 2, 997]]), True),
    (dict(X=8, Y=5, circles=[[2, 3, 1], [5, 4, 1], [2, 1, 1], [5, 4, 1], [3, 2, 1], [5, 2, 2], [7, 1, 1]]), False),
    (dict(X=5, Y=8, circles=[[4, 7, 1]]), False),
    (dict(X=3, Y=4, circles=[[2, 1, 1]]), True),
    (dict(X=3, Y=3, circles=[[1, 1, 2]]), False),
    (dict(X=3, Y=3, circles=[[2, 1, 1], [1, 2, 1]]), False),
]
for e, a in examples:
    print(a, e)
    print(s.canReachCorner(**e))
