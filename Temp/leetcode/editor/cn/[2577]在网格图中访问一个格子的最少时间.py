# 2577 在网格图中访问一个格子的最少时间
# https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Dijkstra
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        g = [[inf] * n for _ in range(m)]
        h = [(0, 0, 0)]
        while h:
            t, r, c = heapq.heappop(h)
            if t > g[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return t
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nt = grid[nr][nc]
                    # 到 (nr,nc) 的时间 t + 1 + 2x >= nt
                    # x >= (nt - 1 - t) / 2
                    # x = (nt - t ) // 2
                    # 到 (nr,nc) 的时间 t + 1 + 2 * ((nt - t)//2)  # 注意运算优先级
                    nt = t + 1 + (0 if nt <= t + 1 else 2 * ((nt - t) // 2))
                    if nt < g[nr][nc]:
                        heapq.heappush(h, (nt, nr, nc))
                        g[nr][nc] = nt


# leetcode submit region end(Prohibit modification and deletion)

# 灵神二分 + BFS
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:  # 无法「等待」
            return -1

        vis = [[-inf] * n for _ in range(m)]

        def check(end_time: int) -> bool:
            vis[-1][-1] = end_time
            q = [(m - 1, n - 1)]
            t = end_time - 1
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):  # 枚举周围四个格子
                        if 0 <= x < m and 0 <= y < n and vis[x][y] != end_time and grid[x][y] <= t:
                            if x == 0 and y == 0: return True
                            vis[x][y] = end_time  # 用二分的值来标记，避免重复创建 vis 数组
                            q.append((x, y))
                t -= 1
            return False

        left = max(grid[-1][-1], m + n - 2) - 1
        right = max(map(max, grid)) + m + n  # 开区间
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right + (right - m - n) % 2
