from typing import List


# 题目：100118. 在树上执行操作以后得到的最大分数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-370/problems/maximum-score-after-applying-operations-on-a-tree/
# 题库：

# class Solution:
#     def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
#         g = [[] for _ in values]
#         g[0].append(-1)  # 给根节点加上一个-1
#         for u, v in edges:
#             g[u].append(v)
#             g[v].append(u)
#
#         # 假设先选取所有的点，然后考虑“还回去”一些点使这个树变健康
#         # 计算“还回去”的最少代价
#         # 遍历这棵树，考虑以 i 为根节点的子树
#         # 1.如果选择“还回去”根节点，就不用继续递归了，（因为都是正整数，后面如果还选择“还回去”肯定会变大，所以后面的就都不用还了，而且已经健康了）
#         # 2.如果不选择“还回去”根节点，就继续递归下去，
#         # 返回所有子树的代价和 与 根节点 的较小值
#         # 3.如果到了叶子节点，说明前面都没有“还回去”，那叶子节点就必须“还回去”。
#         def dfs(i: int, fa: int) -> int:
#             if len(g[i]) == 1:  # i是根节点
#                 return values[i]
#             sub_loss_sum = 0
#             for son in g[i]:
#                 if son != fa:
#                     sub_loss_sum += dfs(son, i)
#             return min(sub_loss_sum, values[i])
#
#         return sum(values) - dfs(0, -1)

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        g = [[] for _ in values]
        g[0].append(-1)  # 给根节点加上一个-1
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 正着考虑
        # 如果以 i 为根的子树，
        # 1. 不择 i，剩下的子树就都选择
        #    values[i]不变0，每条路上都有 i 这个不为0的数，所以剩下的都选
        #    返回子树 i 不包含 i 的节点和
        # 2. 选择 i，递归 i 的子树
        #    返回 dfs(子树) 的和
        # 返回二者的较大值
        # 3. 到了根节点，说明前面都被选择了，为了这条路上和不为 0，必须不能选了
        #    返回 0

        def helper(i: int, fa: int) -> int:
            nonlocal sub_tree_sum
            for son in g[i]:
                if son != fa:
                    sub_tree_sum[i] += helper(son, i)
            return sub_tree_sum[i]

        def dfs(i: int, fa: int) -> int:
            if len(g[i]) == 1:
                return 0
            res = values[i]  # 选择 i，递归下去
            for son in g[i]:
                if son != fa:
                    res += dfs(son, i)
            return max(res, sub_tree_sum[i])

        # 先求出每个子树不包括子树根的和
        sub_tree_sum = values.copy()
        helper(0, -1)
        sub_tree_sum = [s - v for s, v in zip(sub_tree_sum, values)]

        return dfs(0, -1)


s = Solution()
examples = [
    (dict(edges=[[0, 1], [0, 2], [0, 3], [2, 4], [4, 5]], values=[5, 2, 5, 2, 1, 1]), 11),
    (dict(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], values=[20, 10, 9, 7, 4, 3, 5]), 40),
]
for e, a in examples:
    print(a, e)
    print(s.maximumScoreAfterOperations(**e))
