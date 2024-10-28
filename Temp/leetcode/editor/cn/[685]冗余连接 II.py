# 685 冗余连接 II
# https://leetcode.cn/problems/redundant-connection-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/redundant-connection-ii/solutions/416748/rong-yu-lian-jie-ii-by-leetcode-solution
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # n 个节点
        p = list(range(n + 1))  # 并查集的 p
        parent = list(range(n + 1))  # 父节点
        conflict = -1  # 冲突（存在某个节点有两个父节点，附加边在这两个之中）
        cycle = -1  # 环路

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        for i, (a, b) in enumerate(edges):
            if parent[b] != b:  # b 已经哟父节点了
                conflict = i
            else:
                parent[b] = a  # b 的父节点改为 a
                pa, pb = find(a), find(b)
                if pa == pb:
                    cycle = i
                else:
                    p[pa] = pb

        if conflict < 0:
            # 只存在回路，最后造成回路的边是附加边
            return edges[cycle]
        else:
            # 有节点有两个父节点
            u, v = edges[conflict]
            pv = parent[v]
            # 附加边要么是 [pv, v] 要么是 [u, v]
            # 如果有回路，而又因为 [u, v] 被标记为冲突
            # 所以附加边是 [pv, v]
            if cycle >= 0:
                return [pv, v]
            return [u, v]

    # leetcode submit region end(Prohibit modification and deletion)
