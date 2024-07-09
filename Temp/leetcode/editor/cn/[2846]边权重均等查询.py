# 2846 边权重均等查询
# https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/


# leetcode submit region begin(Prohibit modification and deletion)
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

# leetcode submit region end(Prohibit modification and deletion)
