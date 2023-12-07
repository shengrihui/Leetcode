# 2603 收集树中金币
from collections import *
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        deg = list(map(len, g))  # 每个点的度数

        left_edges = n - 1
        # 第一遍，去掉所有没有金币的叶子节点，以及他们去掉后新的没有金币的叶子节点
        q = deque(i for i, (d, c) in enumerate(zip(deg, coins)) if d == 1 and c == 0)  # 初始的叶子节点
        while q:
            leaf = q.popleft()
            deg[leaf] -= 1
            left_edges -= 1
            for y in g[leaf]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)

        # 现在所有叶子节点（度为1的点）都是有金币的节点了
        for i, d in enumerate(deg):
            if d == 1:
                q.append(i)
        left_edges -= len(q)  # 所有到叶子结点的最后一条边
        while q:
            leaf = q.popleft()
            # deg[leaf] -= 1  # 可以不用
            for y in g[leaf]:  # 有金币的叶子节点的邻居节点
                deg[y] -= 1
                if deg[y] == 1:  # 现在y是叶子节点了
                    left_edges -= 1
                # 如果这个时候它的度数不是1，说明他还有别的邻居
        return max(left_edges * 2, 0)


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.collectTheCoins([1, 1, 1, 1, 1, 1, 0, 0], [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [3, 7]]))
