# 2581 统计可能的树根数目
# https://leetcode.cn/problems/count-number-of-possible-root-nodes/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        def h(x, y):  # 哈希
            return x << 17 | y  # 编号最多 10**5

        st = set(h(x, y) for x, y in guesses)
        n = len(edges) + 1  # 节点数量
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        res, cnt = 0, 0

        def dfs(x, fa):
            nonlocal cnt
            for son in g[x]:
                if son == fa:
                    continue
                cnt += h(x, son) in st
                dfs(son, x)

        dfs(0, -1)  # 计算假设以 0 为根的情况下猜对了多少，存在 cnt 中

        def redfs(x, fa, cnt):
            nonlocal res
            if cnt >= k:  # 猜对了，可以以 x 为根
                res += 1
            # 接下来假设根是 son x的子节点
            # 猜对的数量变化：
            # 如果 (x,son) 在 guesses 里，，原来猜对了，现在改了就错了，减 1
            # 如果 (son,x) 在 guesses 里，加 1
            for son in g[x]:
                if son == fa:
                    continue
                redfs(son, x, cnt - (h(x, son) in st) + (h(son, x) in st))

        redfs(0, -1, cnt)
        return res
# leetcode submit region end(Prohibit modification and deletion)
