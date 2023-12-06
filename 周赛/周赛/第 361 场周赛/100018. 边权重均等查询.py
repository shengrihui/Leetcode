from typing import List


# 题目：# 100018. 边权重均等查询
# 题目链接：https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description/
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict
        # 在树中，别说事最短路径了，就是两个点之间的路径也只有唯一的一条（不走回头路）
        neighbors = [[] for _ in range(n)]
        # mp = [[[]] * n for _ in range(n)]
        for u, v, w in edges:
            neighbors[u].append([v, [], [w]])
            neighbors[v].append([u, [], [w]])
            # mp[u][v] =[w]
            # mp[v][u] = [w]
        ans = []
        for a, b in queries:
            q = deque()
            q.append((a, [], []))
            vis = [False] * n
            vis[a] = True
            while q:
                u, au_mid, au_ws = q.popleft()
                if u == b:
                    break
                for v, uv_mid, uv_ws in neighbors[u]:
                    au_ws_copy = au_ws.copy()
                    au_mid_copy = au_mid.copy()
                    # w = mp[a][v]
                    if not vis[v]:  # and mp[u][v]:
                        au_ws_copy.extend(uv_ws)
                        au_mid_copy.extend(uv_mid)
                        q.append((v, au_mid_copy,au_ws_copy))
                        vis[v] = True
                        # if not mp[a][v]:
                        #     mp[a][v] = ws_copy
                        # else:
                        #     if len(mp[a][v])<len(ws_copy):
                        #         mp[a][v] = ws_copy

            print(a, b, "====================================")
            for i, ne in enumerate(mp):
                print(i, ne)

            length = len(au_ws)
            # print(ws)
            d = defaultdict(int)
            for i in ws:
                d[i] += 1
            t = length
            for i in d.values():
                t = min(t, length - i)
            ans.append(t)
        return ans


s = Solution()
examples = [
    # (dict(n=7, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]],
    #       queries=[[0, 3], [3, 6], [2, 6], [0, 6]]), [0, 0, 1, 3]),
    (dict(n=8, edges=[[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]],
          queries=[[4, 6], [0, 4], [6, 5], [7, 4]]), [1, 2, 2, 3]),
    # (dict(n=1, edges=[], queries=[[0, 0]]), [0]),
    # (dict(n=2, edges=[[0, 1, 26]], queries=[[0, 1], [0, 0], [1, 1]]), [0, 0, 0]),
    # (dict(n=6, edges=[[1, 3, 3], [4, 1, 3], [0, 3, 5], [5, 4, 2], [2, 5, 1]], queries=[[2, 0]]), [3]),
]
for e, a in examples:
    print(a, e)
    print(s.minOperationsQueries(**e))
