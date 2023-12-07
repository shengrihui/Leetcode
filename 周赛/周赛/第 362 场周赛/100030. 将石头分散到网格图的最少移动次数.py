from itertools import permutations
from math import inf
from typing import List


# 题目：# 100030. 将石头分散到网格图的最少移动次数
# 题目链接：
# 题库：https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/
# 竞赛：https://leetcode.cn/contest/weekly-contest-362/problems/minimum-moves-to-spread-stones-over-grid/

# BFS超时
# class Solution:
#     def minimumMoves(self, grid: List[List[int]]) -> int:
#         def f(gr):
#             ret = "".join([str(gr[i][j]) for i in range(3) for j in range(3)])
#             return ret
#
#         q = deque()
#         t = f(grid)
#         q.append((t, grid, 0))
#         s = {t}
#         while q:
#             sta, g, c = q.popleft()
#             # print(sta, g, c)
#             if sta == "111111111":
#                 return c
#             for i in range(3):
#                 for j in range(3):
#                     if g[i][j] > 1:
#                         for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#                             ni, nj = i + di, j + dj
#                             if 0 <= ni < 3 and 0 <= nj < 3:
#                                 new_grid = deepcopy(g)
#                                 new_grid[ni][nj] += 1
#                                 new_grid[i][j] -= 1
#                                 t = f(new_grid)
#                                 if t not in s:
#                                     q.append((t, new_grid, c + 1))
#                                     s.add(t)


# DFS全排列
# class Solution:
#     def minimumMoves(self, grid: List[List[int]]) -> int:
#         from_ = []
#         to = []
#         for i, row in enumerate(grid):
#             for j, cnt in enumerate(row):
#                 if cnt == 0:
#                     to.append((i, j))
#                 elif cnt > 1:
#                     from_.extend([(i, j)] * (cnt - 1))
#
#         def dfs(to_list):
#             nonlocal vis, ans, to, from_
#             if len(to_list) == len(from_):
#                 dist = 0
#                 for (fx, fy), (tx, ty) in zip(from_, to_list):
#                     dist += abs(tx - fx) + abs(ty - fy)
#                 ans = min(ans, dist)
#                 return
#             for i, to2 in enumerate(to):
#                 if not vis[i]:
#                     vis[i] = True
#                     to_list.append(to2)
#                     dfs(to_list)
#                     to_list.pop()
#                     vis[i] = False
#
#         ans = inf
#         vis = [False] * len(from_)
#         for i, to2 in enumerate(to):
#             vis[i] = True
#             dfs([to2])
#             vis[i] = False
#
#         return ans

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        from_ = []
        to = []
        for i, row in enumerate(grid):
            for j, cnt in enumerate(row):
                if cnt == 0:
                    to.append((i, j))
                elif cnt > 1:
                    from_.extend([(i, j)] * (cnt - 1))
        ans = inf
        for from2 in permutations(from_):
            dist = 0
            for (fx, fy), (tx, ty) in zip(from2, to):
                dist += abs(tx - fx) + abs(ty - fy)
            ans = min(ans, dist)
        return ans


s = Solution()
examples = [
    (dict(grid=[[1, 1, 0], [1, 1, 1], [1, 2, 1]]), 3),
    (dict(grid=[[1, 3, 0], [1, 0, 0], [1, 0, 3]]), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minimumMoves(**e))
