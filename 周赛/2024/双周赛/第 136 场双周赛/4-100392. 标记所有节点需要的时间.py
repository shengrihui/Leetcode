# 第 136 场双周赛 第 4 题
# 题目：100392. 标记所有节点需要的时间
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-136/problems/time-taken-to-mark-all-nodes/
# 题库：https://leetcode.cn/problems/time-taken-to-mark-all-nodes

from typing import List


# 题目转换：
# x 到 y 之间有一条距离为 2 - y % 2 （奇数 1 偶数 2） 的有向边
# ans[i] 表示以 i 为根的最大距离/深度
#
# 换根DP
class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1  # 节点个数
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 第一遍 DFS 以 0 为根
        # 计算和记录：
        # 1. 子树 x 的最大深度 max_d
        # 2. 子树 x 的次大深度 max_d2
        # 3. 拥有最大深度 max_d 的儿子编号 my
        nodes = [None] * n

        def dfs(x: int, fa: int) -> int:  # 返回最大深度
            max_d = max_d2 = my = 0  # 初始化最大和次大深度以及有最大深度的儿子编号
            for y in g[x]:
                if y == fa:
                    continue
                depth = dfs(y, x) + 2 - y % 2
                if depth > max_d:
                    max_d, max_d2 = depth, max_d
                    my = y
                elif depth > max_d2:
                    max_d2 = depth
            nodes[x] = (max_d, max_d2, my)
            return max_d

        dfs(0, -1)

        ans = [0] * n

        # y 是 x 的儿子
        # 根从 x 变为 y 的时候，
        # y 作为根的最大深度来源：
        # 1. y 子树的最大深度 max_d
        # 2. y->x 之后再加上 x 的各个邻居节点（父节点、y 的兄弟）后的最大深度
        #       1. y 的兄弟节点
        #           如果 y 是 my 加上 x 子树的次大 max_d2
        #           如果 不是，加上 x 子树的最大 max_d
        #       2. x 的父节点之后的最大深度
        #           fromUp 参数，
        #           第一次从 0 节点作为根的时候是 0
        #           后续的 fromUp，就是传入的 fromUP 和兄弟交点取的较大值传下去
        def reroot(x: int, fa: int, fromUp: int) -> None:
            max_d, max_d2, my = nodes[x]
            ans[x] = max(max_d, fromUp)
            for y in g[x]:
                if y == fa:
                    continue
                brother = max_d2 if y == my else max_d
                reroot(y, x, max(fromUp, brother) + 2 - x % 2)

        reroot(0, -1, 0)
        return ans


s = Solution()
examples = [
    (dict(edges=[[0, 1], [0, 2]]), [2, 4, 3]),
    (dict(edges=[[0, 1]]), [1, 2]),
    (dict(edges=[[2, 4], [0, 1], [2, 3], [0, 2]]), [4, 6, 3, 5, 5]),
]
for e, a in examples:
    print(a, e)
    print(s.timeTaken(**e))
