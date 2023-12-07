# 2258 逃离火灾
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maximumMinutes(self, grid: List[List[int]]) -> int:
#         R = 10 ** 9 + 10 ** 5
#         m, n = len(grid), len(grid[0])
#         fire = [[0 if grid[i][j] in [1, 2] else R for j in range(n)] for i in range(m)]
#         q = deque([(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 1])
#         while q:
#             x, y, t = q.popleft()
#             for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < m and 0 <= ny < n and fire[nx][ny] == R:
#                     fire[nx][ny] = t + 1
#                     q.append((nx, ny, t + 1))
#
#         def check(start):
#             v = set()
#             q = deque()
#             if fire[0][0] > start:
#                 q.append((0, 0, start))  # 从 start 这个时间出发
#                 v.add((0, 0))
#             while q:
#                 x, y, t = q.popleft()
#                 for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                     nx, ny = x + dx, y + dy
#                     if nx == m - 1 and ny == n - 1 and fire[nx][ny] >= t + 1:
#                         return True
#                     if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in v and fire[nx][ny] > t + 1:
#                         q.append((nx, ny, t + 1))
#                         v.add((nx,ny))
#             return False
#
#         # l, r = 0, 10 ** 9
#         l, r = 0, min(fire[0][0], 10 ** 9)
#         while l <= r:
#             mid = (r + l) // 2
#             if check(mid):
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return r

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(q: List[Tuple[int, int]]) -> (int, int, int):
            time = [[-1] * n for _ in range(m)]
            for i, j in q:
                time[i][j] = 0
            t = 1
            while q:
                tmp = q
                q = []
                for x, y in tmp:
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and time[nx][ny] == -1:
                            time[nx][ny] = t
                            q.append((nx, ny))
                t += 1
            return time[-1][-1], time[-1][-2], time[-2][-1]

        fire_to_house, f1, f2 = bfs([(i, j) for i, row in enumerate(grid) for j, x in enumerate(row) if x == 1])
        man_to_house, m1, m2 = bfs([(0, 0)])
        if man_to_house == -1:  # 人到不了安全屋
            return -1
        if fire_to_house == -1:  # 火到不了安全屋，人无论怎样都能到
            return 10 ** 9
        d = man_to_house - fire_to_house
        if d > 0:  # 火比人先到（人的时间比火多）
            return -1
        d = -d
        if m1 != -1 and m1 + d < f1 or m2 != -1 and m2 + d < f2:
            # 人比火先到安全屋左边 or 上边的其中一个，并且在那里等了 d 分钟后，仍然比火先到安全屋
            return d
        # 人比火先到安全屋左边 or 上边的其中一个，但等了 d 分钟后火就会到这个格子，所以要在火来的前一步进入安全屋
        return d - 1

# leetcode submit region end(Prohibit modification and deletion)
