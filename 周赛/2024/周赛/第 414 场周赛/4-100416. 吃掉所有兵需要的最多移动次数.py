# 第 414 场周赛 第 4 题
# 题目：100416. 吃掉所有兵需要的最多移动次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-414/problems/maximum-number-of-moves-to-kill-all-pawns/
# 题库：https://leetcode.cn/problems/maximum-number-of-moves-to-kill-all-pawns

from collections import *
from functools import *
from math import inf
from typing import List

dirs = [(i, j) for i in (-2, -1, 1, 2) for j in (-2, -1, 1, 2) if abs(i) + abs(j) == 3]


class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        ps = [[kx, ky]] + positions
        pos_id = {(x, y): i for i, (x, y) in enumerate(ps)}
        n = len(ps)
        N = (1 << n) - 1

        # BFS
        # 求 dis[i][j] i 到 j 的最少移动步数
        dis = [[1000] * n for _ in range(n)]
        for i, (x, y) in enumerate(ps):
            q = deque([(x, y, 0)])
            vis = {(x, y)}
            cnt = 0
            while q and cnt < n:
                u, v, step = q.popleft()
                if (u, v) in pos_id:
                    dis[i][pos_id[(u, v)]] = step
                    cnt += 1
                    if cnt == n:
                        break
                for du, dv in dirs:
                    nu, nv = u + du, v + dv
                    if 0 <= nu < 50 and 0 <= nv < 50 and (nu, nv) not in vis:
                        vis.add((nu, nv))
                        q.append((nu, nv, step + 1))

        # 状态压缩
        # i 上一次选的，mask 已经吃掉的兵
        # mask 初始是 1，因为马看做编号为 0 的兵
        @cache
        def dfs(i: int, mask: int) -> int:
            if mask == N:
                return 0
            alice = mask.bit_count() % 2  # 奇数是轮到 Alice
            res, op = (0, max) if alice else (inf, min)
            for j in range(n):
                if mask >> j & 1 == 0:  # 当前玩家选择 j
                    res = op(res, dfs(j, mask | (1 << j)) + dis[i][j])
            return res

        return dfs(0, 1)


s = Solution()
examples = [
    (dict(kx=1, ky=1, positions=[[0, 0]]), 4),
    (dict(kx=0, ky=2, positions=[[1, 1], [2, 2], [3, 3]]), 8),
    (dict(kx=0, ky=0, positions=[[1, 2], [2, 4]]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.maxMoves(**e))
