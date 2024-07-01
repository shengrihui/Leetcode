# 第 404 场周赛 第 4 题
# 题目：100318. 合并两棵树后的最小直径
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-404/problems/find-minimum-diameter-after-merging-two-trees/
# 题库：https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees

from typing import List


# 如果两个树的直径大小差很大，不管怎么连，最后的结果都是两个树中的较大直径
# 如果两个树的直径差不多，结果是两个树的直径的一半+1
# 选择的两个点是两个树的中点
class Solution:
    def diameter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 树形DP

        res = 0
        """
        def dfs(x: int, fa: int) -> int:
            nonlocal res
            max_len = 0  # 在遍历 y 的时候的最大链长
            for y in g[x]:
                if y != fa:
                    sub_len = dfs(y, x) + 1  # y 这个子树的链长
                    res = max(res, max_len + sub_len)
                    max_len = max(max_len, sub_len)
            return max_len

        dfs(0, -1)
        return res
        """

        def dfs(x: int, fa: int, depth: int) -> None:
            nonlocal res, node
            if depth > res:
                res = depth
                node = x
            for y in g[x]:
                if y != fa:
                    dfs(y, x, depth + 1)

        res = node = -1
        dfs(0, -1, 0)
        res = 0
        dfs(node, -1, 0)
        return res

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        r1 = self.diameter(edges1)
        r2 = self.diameter(edges2)
        return max(r1, r2, (r1 + 1) // 2 + (r2 + 1) // 2 + 1)


s = Solution()
examples = [
    (dict(edges1=[[0, 1], [0, 2], [0, 3]], edges2=[[0, 1]]), 3),
    (dict(edges1=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
          edges2=[[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]), 5),
]
for e, a in examples:
    print(a, e)
    print(s.minimumDiameterAfterMerge(**e))
