from typing import List


# 第 361 场周赛 q4
# 题目：# 100018. 边权重均等查询
# 题目链接：https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description/
# 竞赛：https://leetcode.cn/contest/weekly-contest-361/problems/minimum-edge-weight-equilibrium-queries-in-a-tree

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 建图
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])  # w-1 是因为后面就开26大小的数组
            g[b].append([a, w])

        # 树上倍增
        m = n.bit_length()
        pa = [[-1] * m for _ in range(n)]

        # 深度数组和每个节点上权重统计
        depth = [0] * n  # depth[i] 节点 i 的深度
        cnt = [[] for _ in range(n)]  # cnt[i] 节点 i 到根节点路径上的权重统计
        cnt[0] = [0] * 27

        def dfs(i: int, fa: int) -> None:
            pa[i][0] = fa
            for son, w in g[i]:
                if son != fa:
                    cnt[son] = cnt[i].copy()  # son 到根节点的路，先“继承”一下 son的父节点i 到根节点的路
                    cnt[son][w] += 1  # 再将 i到son 的权重计数 +1
                    depth[son] = depth[i] + 1
                    dfs(son, i)

        dfs(0, -1)
        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

        ans = []
        for x, y in queries:
            path_len = depth[x] + depth[y]  # a 到 b 的路径长度，后面找到 lca 后再减去 depth[lca]*2
            cw = [c1 + c2 for c1, c2 in zip(cnt[x], cnt[y])]
            # lca
            if depth[x] > depth[y]:  # 保证 a 比 b 高
                x, y = y, x
            k = depth[y] - depth[x]
            for j in range(k.bit_length() + 1):
                if (k >> j) & 1:
                    y = pa[y][j]

            if x != y:  # 两个一起往上跳
                for i in range(m - 1, -1, -1):  # 以尽可能大的步数往上
                    if (px := pa[x][i]) != (py := pa[y][i]):  # 两个一样就不跳
                        x, y = px, py
                x = pa[x][0]  # 结束后 lca 是父节点
            lca = x
            path_len -= 2 * depth[lca]
            for i, c in enumerate(cnt[lca]):
                cw[i] -= 2 * c
            ans.append(path_len - max(cw))
        return ans


s = Solution()
examples = [
    # (dict(n=7, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]],
    #       queries=[[0, 3], [3, 6], [2, 6], [0, 6]]), [0, 0, 1, 3]),
    (dict(n=8, edges=[[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]],
          queries=[[4, 6], [0, 4], [6, 5], [7, 4]]), [1, 2, 2, 3]),
    (dict(n=1, edges=[], queries=[[0, 0]]), [0]),
    (dict(n=2, edges=[[0, 1, 26]], queries=[[0, 1], [0, 0], [1, 1]]), [0, 0, 0]),
    (dict(n=6, edges=[[1, 3, 3], [4, 1, 3], [0, 3, 5], [5, 4, 2], [2, 5, 1]], queries=[[2, 0]]), [3]),
]
for e, a in examples:
    print(a, e)
    print(s.minOperationsQueries(**e))
    print()
