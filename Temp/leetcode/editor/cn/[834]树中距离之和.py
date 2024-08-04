# 834 树中距离之和
# https://leetcode.cn/problems/sum-of-distances-in-tree/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = [0] * n
        size = [1] * n  # 每一棵子树的大小，初始化为 1

        def dfs(x: int, fa: int, depth: int) -> None:
            ans[0] += depth  # 0 到 x 的距离是 depth 加到 ans[0] 里
            for y in g[x]:
                if y != fa:
                    dfs(y, x, depth + 1)
                    size[x] += size[y]  # x 子树的大小加上 y 子树的大小

        dfs(0, -1, 0)

        # y 是 x 的儿子
        # 当根从 x 变到 y 的时候，
        # y 子树上的节点到 y 的距离都 -1 （和到 x 比）一共 size[y]
        # 非 y 子树上的节点到 y 的距离都 +1 一共 n-size[y]
        # 所以 ans[y] = ans[x] - size[y] + n - size[y] = ans[x] + n - 2*size[y]
        def reroot(x: int, fa: int) -> None:
            for y in g[x]:
                if y != fa:
                    ans[y] = ans[x] + n - 2 * size[y]
                    reroot(y, x)

        reroot(0, -1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
