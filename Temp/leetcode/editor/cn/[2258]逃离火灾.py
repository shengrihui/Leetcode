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


# 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一： 
# 
#  
#  0 表示草地。 
#  1 表示着火的格子。 
#  2 表示一座墙，你跟火都不能通过这个格子。 
#  
# 
#  一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。每次你
# 移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。 
# 
#  请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你 总
# 是 能到达安全屋，请你返回 10⁹ 。 
# 
#  注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。 
# 
#  如果两个格子有共同边，那么它们为 相邻 格子。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0
# ,0,0,0,0,0,0]]
# 输出：3
# 解释：上图展示了你在初始位置停留 3 分钟后的情形。
# 你仍然可以安全到达安全屋。
# 停留超过 3 分钟会让你无法安全到达安全屋。 
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
# 输出：-1
# 解释：上图展示了你马上开始朝安全屋移动的情形。
# 火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。
# 所以返回 -1 。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [[0,0,0],[2,2,0],[1,2,0]]
# 输出：1000000000
# 解释：上图展示了初始网格图。
# 注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。
# 所以返回 10⁹ 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  2 <= m, n <= 300 
#  4 <= m * n <= 2 * 10⁴ 
#  grid[i][j] 是 0 ，1 或者 2 。 
#  grid[0][0] == grid[m - 1][n - 1] == 0 
#  
# 
#  Related Topics 广度优先搜索 数组 二分查找 矩阵 👍 58 👎 0
