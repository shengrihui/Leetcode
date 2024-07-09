# 2742 给墙壁刷油漆
# https://leetcode.cn/problems/painting-the-walls/

# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            # 前 i 面墙，有 j 个可以免费刷的时间，最小花费
            if i < j:  # 剩下的墙都可以免费刷
                return 0
            if i < 0:
                return inf
            return min(dfs(i - 1, j + time[i]) + cost[i], dfs(i - 1, j - 1))

        return dfs(len(cost) - 1, 0)
"""

# 0-1 背包
"""
付费墙面数  + 免费墙面数 = n
付费墙面时间 >= 免费墙面数 = n - 付费墙面数
付费墙面时间 + 付费墙面数 >= n
sum_{i=付费的墙面}{time[i] + 1} >= n
0-1 背包问题：
每个物品的体积是 time[i]+1 ，至少要装容量 n ，最小化花费
dfs(i,j) 前 i 个物品，剩余 j 的容量
转移：
    dfs(i,j) = min(dfs(i - 1, j - time[i] - 1) + cost[i], dfs(i - 1, j))
递归边界：
    j <= 0 return 0 ,满足了“容量至少n",是个合法的方案，
    i < 0 return inf 墙面没了，但容量还没有 n 
递归入口：
    dfs(n,n)


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if j <= 0:
                return 0
            if i < 0:
                return inf
            return min(dfs(i - 1, j - time[i] - 1) + cost[i], dfs(i - 1, j))

        n = len(cost)
        return dfs(n-1, n)
"""


# 转为递推
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        f = [0] + [inf] * n  # f[0] j=0 的时候
        for c, t in zip(cost, time):  # 遍历所有“物品”
            for j in range(n, 0, -1):
                # f[j] = min(f[j], f[max(j - t - 1, 0)] + c)
                tmp = f[0 if j - t - 1 < 0 else j - t - 1] + c
                if tmp < f[j]:
                    f[j] = tmp
        return f[n]
# leetcode submit region end(Prohibit modification and deletion)
