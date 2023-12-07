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


# 现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 
# edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。 
# 
#  每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。 
# 
#  给定路径的 价格总和 是该路径上所有节点的价格之和。 
# 
#  另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何
# 你喜欢的路径前往节点 endi 。 
# 
#  在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。 
# 
#  返回执行所有旅行的最小价格总和。 
# 
#  
# 
#  示例 1： 
#  输入：n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,
# 1],[2,3]]
# 输出：23
# 解释：
# 上图表示将节点 2 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 、2 和 3 并使其价格减半后的树。
# 第 1 次旅行，选择路径 [0,1,3] 。路径的价格总和为 1 + 2 + 3 = 6 。
# 第 2 次旅行，选择路径 [2,1] 。路径的价格总和为 2 + 5 = 7 。
# 第 3 次旅行，选择路径 [2,1,3] 。路径的价格总和为 5 + 2 + 3 = 10 。
# 所有旅行的价格总和为 6 + 7 + 10 = 23 。可以证明，23 是可以实现的最小答案。 
# 
#  示例 2： 
#  输入：n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
# 输出：1
# 解释：
# 上图表示将节点 0 视为根之后的树结构。第一个图表示初始树，第二个图表示选择节点 0 并使其价格减半后的树。 
# 第 1 次旅行，选择路径 [0] 。路径的价格总和为 1 。 
# 所有旅行的价格总和为 1 。可以证明，1 是可以实现的最小答案。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  edges.length == n - 1 
#  0 <= ai, bi <= n - 1 
#  edges 表示一棵有效的树 
#  price.length == n 
#  price[i] 是一个偶数 
#  1 <= price[i] <= 1000 
#  1 <= trips.length <= 100 
#  0 <= starti, endi <= n - 1 
#  
# 
#  Related Topics 树 深度优先搜索 图 数组 动态规划 👍 73 👎 0
