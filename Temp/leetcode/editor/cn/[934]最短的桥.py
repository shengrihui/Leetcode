# 934 最短的桥
# https://leetcode.cn/problems/shortest-bridge/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island = deque()
        edges = set()  # 第 1 个岛的边界
        for x in range(n * n):  # 进入第 1 个岛
            i, j = x // n, x % n
            if grid[i][j] == 1:
                island.append((i, j))
                edges.add((i, j))
                grid[i][j] = -1
                break
        # BFS 找完整的第 1 岛
        while island:
            i, j = island.popleft()
            for ni, nj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        island.append((ni, nj))
                        grid[ni][nj] = -1
                    elif grid[ni][nj] == 0:  # (i,j)是岛的边界
                        edges.add((i, j))
        # 以边界为起点，BFS 找另一个岛，遍历过的改为 -1
        q = deque(edges)
        ans = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for ni, nj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return ans
                        if grid[ni][nj] == 0:
                            q.append((ni, nj))
                            grid[ni][nj] = -1
            ans += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
