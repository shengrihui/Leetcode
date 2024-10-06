# 第 418 场周赛 第 3 题
# 题目：100431. 构造符合图结构的二维矩阵
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-418/problems/construct-2d-grid-matching-graph-layout/
# 题库：https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout

from collections import deque
from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 找四个角
        # 如果 len(edges) == n - 1 那么只能是一行（或者一列），
        # 那么角的邻居只有 1 个，否则角有 2 个邻居
        corner_mn = 1 if len(edges) == n - 1 else 2
        corner = [i for i in range(n) if len(g[i]) == corner_mn]

        first_row = []
        first = corner[0]  # 找一个作为起点，最左上角
        q = deque([(first, [first])])  # (当前点，是行还是列过来的）
        vis = {first}
        corner = set(corner[1:])  # 剩下的角
        while q:
            u, path = q.popleft()
            if u in corner:
                first_row = path
                break
            for i, v in enumerate(g[u]):
                if v not in vis and len(g[v]) < 4:
                    vis.add(v)
                    q.append((v, path + [v]))

        col = len(first_row)  # 列数
        ans = [first_row]
        # 填答案
        vis = set(first_row)
        while len(vis) < n:
            nxt_row = []
            for j in range(col):
                for x in g[ans[- 1][j]]:
                    if x not in vis:
                        vis.add(x)
                        nxt_row.append(x)
                        break
            ans.append(nxt_row)
        return ans


"""
class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # 每种度数选一个点
        deg_to_node = [-1] * 5
        for x, e in enumerate(g):
            deg_to_node[len(e)] = x

        if deg_to_node[1] != -1:
            # 答案只有一列
            row = [deg_to_node[1]]
        elif deg_to_node[4] == -1:
            # 答案只有两列
            x = deg_to_node[2]
            for y in g[x]:
                if len(g[y]) == 2:
                    row = [x, y]
                    break
        else:
            # 答案至少有三列
            x = deg_to_node[2]
            row = [x]
            pre = x
            x = g[x][0]
            while len(g[x]) > 2:
                row.append(x)
                for y in g[x]:
                    if y != pre and len(g[y]) < 4:
                        pre = x
                        x = y
                        break
            row.append(x)

        ans = [[] for _ in range(n // len(row))]
        ans[0] = row
        vis = [False] * n
        for x in row:
            vis[x] = True
        for i in range(1, len(ans)):
            for x in ans[i - 1]:
                for y in g[x]:
                    # x 上左右的邻居都访问过了，没访问过的邻居只会在 x 下面
                    if not vis[y]:
                        vis[y] = True
                        ans[i].append(y)
                        break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/construct-2d-grid-matching-graph-layout/solutions/2940537/fen-lei-tao-lun-zhu-xing-gou-zao-by-endl-v3x0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
s = Solution()
examples = [
    # (dict(n=6, edges=[[0, 1], [0, 2], [0, 4], [1, 3], [2, 5], [3, 4], [4, 5]]), []),
    # (dict(n=4, edges=[[0, 1], [0, 2], [1, 3]]), []),
    (dict(n=4, edges=[[0, 1], [0, 2], [1, 3], [2, 3]]), [[3, 1], [2, 0]]),
    (dict(n=5, edges=[[0, 1], [1, 3], [2, 3], [2, 4]]), [[4, 2, 3, 1, 0]]),
    (dict(n=9, edges=[[0, 1], [0, 4], [0, 5], [1, 7], [2, 3], [2, 4], [2, 5], [3, 6], [4, 6], [4, 7], [6, 8], [7, 8]]),
     [[8, 6, 3], [7, 4, 2], [1, 0, 5]]),
]
for e, a in examples:
    print(a, e)
    print(s.constructGridLayout(**e))
