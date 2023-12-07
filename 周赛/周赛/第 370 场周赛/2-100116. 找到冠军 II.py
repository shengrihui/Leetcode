from typing import List


# 题目：100116. 找到冠军 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-370/problems/find-champion-ii/
# 题库：https://leetcode.cn/problems/find-champion-ii/description/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for u, v in edges:
            indeg[v] += 1
        ans = [i for i, d in enumerate(indeg) if d == 0]
        if len(ans) == 1:
            return ans[0]
        return -1


# class Solution:
#     def findChampion(self, n: int, edges: List[List[int]]) -> int:
#         mp = [[False] * n for _ in range(n)]
#         for a, b in edges:
#             mp[a][b] = True
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     mp[i][j] |= mp[i][k] and mp[k][j]
#         ans = -1
#         for i, row in enumerate(mp):
#             if sum(row) == n - 1:
#                 if ans != -1:
#                     return -1
#                 ans = i
#         return ans


s = Solution()
examples = [
    (dict(n=3, edges=[[0, 1], [1, 2]]), 0),
    (dict(n=4, edges=[[0, 2], [1, 3], [1, 2]]), -1),
    (dict(n=2, edges=[[1, 0]]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.findChampion(**e))
