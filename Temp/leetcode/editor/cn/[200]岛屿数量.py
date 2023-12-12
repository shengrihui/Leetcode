# 200 岛屿数量
# https://leetcode.cn/problems/number-of-islands/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         n, m = len(grid), len(grid[0])
#         q = deque()
#         vis = [[grid[i][j] == "0" for j in range(m)] for i in range(n)]
#         ans = 0
#         for i in range(n):
#             for j in range(m):
#                 if vis[i][j]:
#                     continue
#                 q.append((i, j))
#                 vis[i][j] = True
#                 while q:
#                     ii, jj = q.popleft()
#                     for ni, nj in [(ii - 1, jj), (ii + 1, jj), (ii, jj - 1), (ii, jj + 1)]:
#                         if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj]:
#                             q.append((ni, nj))
#                             vis[ni][nj] = True
#                 ans += 1
#         return ans

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        total = n * m
        p = list(range(total))

        def find(x: int) -> int:
            nonlocal p
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in range(n):
            for j in range(m):
                x = i * m + j
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ni < n and 0 <= nj < m and grid[i][j] == grid[ni][nj] == "1":
                        p[find(x)] = find(ni * m + nj)
        return len(set([find(i) for i in range(total) if grid[i // m][i % m] == "1"]))

# leetcode submit region end(Prohibit modification and deletion)
