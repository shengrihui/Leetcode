# 2617 网格图中最少访问的格子数
# https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/

from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        col_hs = [[] for _ in grid[0]]
        for i, row in enumerate(grid):
            row_h = []
            # g = row[j] = grid[i][j]
            # col_h = col_h[j] 第 j 列的最小堆
            for j, (g, col_h) in enumerate(zip(row, col_hs)):
                # 以行最小堆为例
                # 堆中元素 (f , gg + jj)
                # f 到 grid[i][jj] = gg 的最小步数
                # 如果堆顶的元素从 grid[i][jj] 能到 grid[i][j]
                # 也就是 gg + jj >= j
                # 那到 grid[i][j] 的最小步数就是 f+1 (行里走）
                # 再和列最小取较小值
                #
                # 两个循环就是在去掉堆顶到不了 [i][j] 的
                while row_h and row_h[0][1] < j:
                    heapq.heappop(row_h)
                while col_h and col_h[0][1] < i:
                    heapq.heappop(col_h)
                f = inf if i or j else 1  # 只有起点是1
                if col_h: f = col_h[0][0] + 1  # 可以从上面来
                if row_h: f = min(f, row_h[0][0] + 1)
                if g and f < inf:
                    # grid[i][j] = 0 没法走啦
                    # f == inf  到不了 grid[i][j]
                    # 入堆 (f,最远到的地方)
                    heapq.heappush(row_h, (f, g + j))
                    heapq.heappush(col_h, (f, g + i))
        return f if f < inf else -1

# 双向 BFS
# class Solution:
#     def minimumVisitedCells(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         if m == n == 1: return 1
#         forward = deque([(0, 0)])
#         backward = deque([(m - 1, n - 1)])
#         forward_vis = {(0, 0)}
#         backward_vis = {(m - 1, n - 1)}
#         step = 1
#         # print(*grid, sep="\n")
#         while forward and backward:
#             if len(forward) <= len(backward):
#                 for _ in range(len(forward)):
#                     i, j = forward.popleft()
#                     x = grid[i][j]
#                     # 向右
#                     for k in range(j, min(n, x + j + 1)):
#                         if (i, k) in backward_vis:
#                             return step + 1
#                         if (i, k) not in forward_vis:
#                             forward.append((i, k))
#                             forward_vis.add((i, k))
#                     # 向下
#                     for k in range(i, min(m, x + i + 1)):
#                         if (k, j) in backward_vis:
#                             return step + 1
#                         if (k, j) not in forward_vis:
#                             forward.append((k, j))
#                             forward_vis.add((k, j))
#             else:
#                 for _ in range(len(backward)):
#                     i, j = backward.popleft()
#                     # 行
#                     for k in range(j, -1, -1):
#                         if grid[i][k] + k >= j:
#                             if (i, k) in forward_vis:
#                                 return step + 1
#                             if (i, k) not in backward_vis:
#                                 backward.append((i, k))
#                                 backward_vis.add((i, k))
#                     # 列
#                     for k in range(i, -1, -1):
#                         if grid[k][j] + k >= i:
#                             if (k, j) in forward_vis:
#                                 return step + 1
#                             if (k, j) not in backward_vis:
#                                 backward.append((k, j))
#                                 backward_vis.add((k, j))
#             # print(forward, backward)
#             step += 1
#         return -1
# BFS
# class Solution:
#     def minimumVisitedCells(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         q = deque([(0, 0)])
#         vis = [[0] * n for _ in range(m)]
#         vis[0][0] = 1
#         step = 1
#         while q:
#             for _ in range(len(q)):
#                 i, j = q.popleft()
#                 if i == m - 1 and j == n - 1:
#                     return step
#                 x = grid[i][j]
#                 # 向右
#                 for k in range(j, min(n, x + j + 1)):
#                     if vis[i][k] == 0:
#                         q.append((i, k))
#                         vis[i][k] = 1
#                 # 向下
#                 for k in range(i, min(m, x + i + 1)):
#                     if vis[k][j] == 0:
#                         q.append((k, j))
#                         vis[k][j] = 1
#             step += 1
#         return -1
# leetcode submit region end(Prohibit modification and deletion)
