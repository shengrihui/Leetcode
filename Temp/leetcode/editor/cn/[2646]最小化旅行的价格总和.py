# 2646 最小化旅行的价格总和
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        cnt = [0] * n  # 每个节点会经过多少次
        for start, end in trips:
            # DFS
            # 从 start 开始DFS，每一个节点 i 遍历它的子节点 j，不断“递”（深入）
            # 如果某一条路到了 end ，则返回 True，并在“归”的时候给路径上的 cnt 加1
            # 如果遍历了所有节点 j 都未能 return 说明这个 i 不在 start 到 end 的路径上
            def cnt_dfs(i: int, fa: int) -> bool:
                if i == end:
                    cnt[i] += 1
                    return True
                for j in g[i]:
                    if j != fa and cnt_dfs(j, i):
                        cnt[i] += 1
                        return True
                return False

            cnt_dfs(start, -1)
            # BFS
            """
            q = deque([(start, [start])])
            while q:
                node, path = q.popleft()
                if node == end:
                    for i in path:
                        cnt[i] += 1
                    break
                for son in g[node]:
                    if son not in path:
                        q.append((son, path + [son]))
            """

        # 现在节点 i 需要经过 cnt[i] 次
        # 那就相当于 i 节点的价格变成了 prices[i] * cnt[i] ，
        # 从未访问过的节点的价格就变成了 0
        # 现在就是要选一部分不相邻的节点，将他们的价格减半，使总和最小
        def dfs(x: int, fa: int) -> (int, int):
            not_halve = price[x] * cnt[x]  # x 节点的“新”价格
            halve = not_halve // 2  # 假如选择 x 价格减半
            for y in g[x]:
                if y != fa:
                    nh, h = dfs(y, x)
                    not_halve += nh if nh < h else h  # 如果 x 不选择减半，那 y 既可以减半也可以不减半，取较小值
                    halve += nh  # x 选择减半，y 只能不减半
            return not_halve, halve

        return min(dfs(0, -1))
# leetcode submit region end(Prohibit modification and deletion)
