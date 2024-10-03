# 1928 规定时间内到达终点的最小花费
# https://leetcode.cn/problems/minimum-cost-to-reach-destination-in-time/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        # f[t][i] 用 t 时间到 i 的最少费用
        f = [[inf] * n for _ in range(maxTime + 1)]
        f[0][0] = passingFees[0]
        for t in range(1, maxTime + 1):
            for i, j, c in edges:
                if c <= t:
                    f[t][i] = min(f[t][i], f[t - c][j] + passingFees[i])  # j 到 i 更新 f[t][i]
                    f[t][j] = min(f[t][j], f[t - c][i] + passingFees[j])  # i 到 j 更新 f[t][j]
        ans = min(f[t][-1] for t in range(1, maxTime + 1))
        return ans if ans != inf else -1


# 有错
"""
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        d = defaultdict(list)
        for x, y, t in edges:
            d[x].append((y, t))
            d[y].append((x, t))
        q = deque([(0, 0, passingFees[0])])
        n = len(passingFees)
        fee = [inf] * n
        fee[0] = passingFees[0]
        while q:
            x, t, f = q.popleft()
            # if f > fee[x]:
            #     continue
            for nx, dt in d[x]:
                nt, nf = t + dt, f + passingFees[nx]
                if nt > maxTime or nf >= fee[nx]:
                    continue
                fee[nx] = nf
                q.append((nx, nt, nf))
        return fee[-1] if fee[-1] != inf else -1
"""
# leetcode submit region end(Prohibit modification and deletion)
