# 1553 吃掉 N 个橘子的最少天数
# https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/

# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(n: int):
            if n <= 1:
                return n
            return min(dfs(n // 2) + n % 2, dfs(n // 3) + n % 3) + 1

        return dfs(n)
"""


# Dijkstra
# x 到 x // 3 之间有一条 x mod 3 + 1 的边
# x 到 x // 2 之间有一条 x mod 2 + 1 的边
# 1 到 0 之间有 1 的边
# 求 n 到 0 的最短路
class Solution:
    def minDays(self, n: int) -> int:
        dis = defaultdict(lambda: inf)  # dis[x] n 到 x 的距离
        h = [(0, n)]  # [到 x 的距离 , x]
        while True:
            dx, x = heapq.heappop(h)
            if x <= 1:
                return dx + x  # 到 x 的加上 1/0
            if dx > dis[x]:  # 被更新过
                continue
            for d in 2, 3:
                y = x // d  # 下一个节点，x 到 y
                dy = x % d + 1 + dx
                if dy < dis[y]:  # 更新到 y 的最短路
                    dis[y] = dy
                    heapq.heappush(h, (dy, y))

# leetcode submit region end(Prohibit modification and deletion)
