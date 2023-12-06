# 2316 统计无向图中无法互相到达点对数
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]]) -> int:
#         mp = [[False] * n for _ in range(n)]
#         for a, b in edges:
#             mp[a][b] = True
#             mp[b][a] = True
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     mp[i][j] |= mp[i][k] and mp[k][j]
#                     mp[j][i] = mp[i][j]
#         ans = 0
#         for i in range(n):
#             for j in range(i):
#                 ans += not mp[i][j]
#         return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        mp = [[] for _ in range(n)]
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
        a = []
        vis = [False] * n

        def bfs(s):
            nonlocal vis
            cnt = 1
            q = deque()
            q.append(s)
            vis[s] = True
            while q:
                m = q.popleft()
                for i in mp[m]:
                    if not vis[i]:
                        q.append(i)
                        vis[i] = True
                        cnt += 1
            return cnt

        ans = 0
        for i in range(n):
            if not vis[i]:
                c = bfs(i)
                ans += c * (n - c)
        return ans // 2

    # leetcode submit region end(Prohibit modification and deletion)

# 给你一个整数 n ，表示一张 无向图 中有 n 个节点，编号为 0 到 n - 1 。同时给你一个二维整数数组 edges ，其中 edges[i] = [
# ai, bi] 表示节点 ai 和 bi 之间有一条 无向 边。 
# 
#  请你返回 无法互相到达 的不同 点对数目 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 3, edges = [[0,1],[0,2],[1,2]]
# 输出：0
# 解释：所有点都能互相到达，意味着没有点对无法互相到达，所以我们返回 0 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# 输出：14
# 解释：总共有 14 个点对互相无法到达：
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6]
# ,[5,6]]
# 所以我们返回 14 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10⁵ 
#  0 <= edges.length <= 2 * 10⁵ 
#  edges[i].length == 2 
#  0 <= ai, bi < n 
#  ai != bi 
#  不会有重复边。 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 61 👎 0
