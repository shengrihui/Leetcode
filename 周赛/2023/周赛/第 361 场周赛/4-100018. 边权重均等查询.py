from typing import List
from collections import deque, defaultdict, Counter

# 第 364 场周赛 q4
# 题目：# 100018. 边权重均等查询
# 题目链接：https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description/
# 竞赛：https://leetcode.cn/contest/weekly-contest-361/problems/minimum-edge-weight-equilibrium-queries-in-a-tree

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:



s = Solution()
examples = [
    (dict(n=7, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]],
          queries=[[0, 3], [3, 6], [2, 6], [0, 6]]), [0, 0, 1, 3]),
    (dict(n=8, edges=[[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]],
          queries=[[4, 6], [0, 4], [6, 5], [7, 4]]), [1, 2, 2, 3]),
    (dict(n=1, edges=[], queries=[[0, 0]]), [0]),
    (dict(n=2, edges=[[0, 1, 26]], queries=[[0, 1], [0, 0], [1, 1]]), [0, 0, 0]),
    (dict(n=6, edges=[[1, 3, 3], [4, 1, 3], [0, 3, 5], [5, 4, 2], [2, 5, 1]], queries=[[2, 0]]), [3]),
]
for e, a in examples:
    print(a, e)
    print(s.minOperationsQueries(**e))
