# 第 410 场周赛 第 2 题
# 题目：100354. 统计好节点的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-410/problems/count-the-number-of-good-nodes/
# 题库：https://leetcode.cn/problems/count-the-number-of-good-nodes

from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        def dfs(x: int, fa: int) -> int:
            st = set()
            total = 0
            for y in g[x]:
                if y != fa:
                    y_num = dfs(y, x)
                    total += y_num
                    st.add(y_num)
            if len(st) <= 1:
                nonlocal ans
                ans += 1
            return total + 1

        ans = 0
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        dfs(0, -1)
        return ans


s = Solution()
examples = [
    (dict(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]), 7),
    (dict(edges=[[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]), 6),
    (dict(edges=[[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10], [9, 12], [10, 11]]),
     12),
]
for e, a in examples:
    print(a, e)
    print(s.countGoodNodes(**e))
