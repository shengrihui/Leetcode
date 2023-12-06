from functools import cache
from typing import List
from collections import *
from itertools import *
from math import *


# 题目：100108. 收集所有金币可获得的最大积分
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-369/problems/maximum-points-after-collecting-coins-from-all-nodes/
# 题库：https://leetcode.cn/problems/maximum-points-after-collecting-coins-from-all-nodes/solutions/2503152/shu-xing-dp-ji-yi-hua-sou-suo-by-endless-phzx/

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges)
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        @cache
        def dfs(fa, now, c):
            res1 = (coins[now] >> c) - k
            res2 = coins[now] >> (c + 1)
            for son in g[now]:
                if son == fa:
                    continue
                res1 += dfs(now, son, c)
                if c + 1 < 13:  # coin[i]<=10^4，最多右移13次就为0了(10**4一共14位）
                    res2 += dfs(now, son, c + 1)
            return max(res1, res2)

        return dfs(-1, 0, 0)


#
# class Solution:
#     def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
#         n = len(edges)
#         g = [[] for _ in range(n + 1)]
#         for a, b in edges:
#             g[a].append(b)
#             g[b].append(a)
#
#         # j（上面的c）数量只有14个，所以单独开俩数组记录j分别是0到13时候的情况
#         # 返回一个长度为14的数组
#         def dfs(fa: int, now: int) -> List[int]:
#             res1 = [0] * 14
#             res2 = [0] * 14
#             for son in g[now]:
#                 if son == fa:
#                     continue
#                 r = dfs(now, son)
#                 for j in range(14):
#                     res1[j] += r[j]
#                     if j < 13:  # coin[i]<=10^4，最多右移13次就为0了(10**4一共14位）
#                         res2[j] += r[j + 1]
#             for j in range(14):
#                 res1[j] = max(res1[j] + (coins[now] >> j) - k,
#                               res2[j] + (coins[now] >> (j + 1)))
#             return res1
#
#         return dfs(-1, 0)[0]  # 必须是0，相当于上一个方法里的那个0


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges)
        g = [[] for _ in range(n + 1)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # j（上面的c）数量只有14个，所以单独开俩数组记录j分别是0到13时候的情况
        # 返回一个长度为14的数组
        def dfs(fa: int, now: int) -> List[int]:
            res1 = [(coins[now] >> j) - k for j in range(14)]
            res2 = [coins[now] >> (j + 1) for j in range(14)]
            for son in g[now]:
                if son == fa:
                    continue
                r = dfs(now, son)
                for j in range(14):
                    res1[j] += r[j]
                    if j < 13:  # coin[i]<=10^4，最多右移13次就为0了(10**4一共14位）
                        res2[j] += r[j + 1]
            return [r1 if r1 > r2 else r2 for r1, r2 in zip(res11, res2)]

        return dfs(-1, 0)[0]  # 必须是0，相当于上一个方法里的那个0


s = Solution()
examples = [
    (dict(edges=[[0, 1], [1, 2], [2, 3]], coins=[10, 10, 3, 3], k=5), 11),
    (dict(edges=[[0, 1], [1, 2], [2, 3]], coins=[10, 10, 3, 10], k=5), -1),
    (dict(edges=[[0, 1], [0, 2]], coins=[8, 4, 4], k=0), 16),
    (dict(edges=[[1, 0], [2, 1], [3, 1]], coins=[8, 2, 7, 1], k=2), 11),
]
for e, a in examples:
    print(a, e)
    print(s.maximumPoints(**e))
