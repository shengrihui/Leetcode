# 第 139 场双周赛 第 2 题
# 题目：100414. 穿越网格图的安全路径
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-139/problems/find-a-safe-walk-through-a-grid/
# 题库：https://leetcode.cn/problems/find-a-safe-walk-through-a-grid

from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dis = [[0] * m for _ in range(n)]
        dis[0][0] = health - grid[0][0]
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if x == n - 1 and y == m - 1:
                return True
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nh = dis[x][y] - grid[nx][ny]
                    if nh > dis[nx][ny]:
                        q.append((nx, ny))
                        dis[nx][ny] = nh
        return False


s = Solution()
examples = [
    (dict(grid=[[1, 1, 1, 1]], health=4), False),
    (dict(grid=[[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], health=3), False),
    (dict(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5), True),
]
for e, a in examples:
    print(a, e)
    print(s.findSafeWalk(**e))
