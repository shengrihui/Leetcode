import copy
from math import inf
from typing import List


# 题目：100140. 关闭分部的可行集合数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-119/problems/number-of-possible-sets-of-closing-branches/
# 题库：https://leetcode.cn/problems/number-of-possible-sets-of-closing-branches

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf if i != j else 0 for j in range(n)] for i in range(n)]
        for u, v, w in roads:
            g[u][v] = g[v][u] = min(g[u][v], w)

        ans = 1  # 全部关掉肯定行
        for s in range((1 << n) - 1):
            gg = copy.deepcopy(g)
            for b in range(n):
                if (s >> b) & 1:  # 第 b 个分部关掉，不可达
                    for i in range(n):
                        gg[b][i] = gg[i][b] = inf
            # 最短路
            for k in range(n):
                # if (s >> k) & 1: continue
                for i in range(n):
                    # if (s >> i) & 1: continue
                    for j in range(n):
                        gg[i][j] = min(gg[i][j], gg[i][k] + gg[k][j])
            flag, i = True, 0
            for i in range(n):
                if (s >> i) & 1:                    continue
                for j in range(n):
                    if (s >> j) & 1:                        continue
                    if gg[i][j] > maxDistance:
                        flag = False
                        break
                if not flag: break
            ans += flag
        return ans


s = Solution()
examples = [
    (dict(n=3, maxDistance=5, roads=[[0, 1, 2], [1, 2, 10], [0, 2, 10]]), 5),
    (dict(n=3, maxDistance=5, roads=[[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]), 7),
    (dict(n=1, maxDistance=10, roads=[]), 2),
    (dict(n=3, maxDistance=3, roads=[[2, 0, 14], [1, 0, 15], [1, 0, 7]]), 4),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfSets(**e))
