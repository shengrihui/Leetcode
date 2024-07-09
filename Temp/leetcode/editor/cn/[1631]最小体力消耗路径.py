# 1631 最小体力消耗路径
# https://leetcode.cn/problems/path-with-minimum-effort/


# 二分+ dfs
# 在 [最小,最大] 相邻两个格子的高度绝对值 之间进行二分
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        if row * col == 1:  # 特判一下~
            return 0
        left, right = inf, 0
        for i in range(row):
            for j in range(col):
                if i > 0:
                    d = abs(heights[i][j] - heights[i - 1][j])
                    left = min(left, d)
                    right = max(right, d)
                if j > 0:
                    d = abs(heights[i][j] - heights[i][j - 1])
                    left = min(left, d)
                    right = max(right, d)

        # 二分的 check 函数，也是 dfs
        # 返回在最大高度差绝对值为 mid 的情况下能否走到终点
        def check(mid: int, x: int, y: int) -> bool:
            nonlocal vis
            if x == row - 1 and y == col - 1:
                return True
            vis.add((x, y))
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (nx, ny) not in vis and 0 <= nx < row and 0 <= ny < col and \
                        abs(heights[x][y] - heights[nx][ny]) <= mid:
                    if check(mid, nx, ny):
                        return True
            return False

        while left <= right:
            mid = (left + right) // 2
            vis = set()
            if check(mid, 0, 0):
                right = mid - 1
            else:
                left = mid + 1
        return left


# Dijkstra
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        dist = [[inf] * col for _ in range(row)]  # dist[i][j] 表示起点到 (i,j) 的 不同路径上中最大的高度差 的最小值
        dist[0][0] = 0  # 初始 起点到起点是0，其余为 inf
        q = [(0, 0, 0)]
        vis = set()  # 没开多少
        while True:
            d, x, y = heapq.heappop(q)
            if x == row - 1 and y == col - 1:
                return d
            vis.add((x, y))
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (nx, ny) not in vis and 0 <= nx < row and 0 <= ny < col and \
                        (nd := max(d, abs(heights[x][y] - heights[nx][ny]))) < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(q, (nd, nx, ny))


# leetcode submit region begin(Prohibit modification and deletion)
# 并查集
# 每个格子看作是图的一个点，相邻格子之间有边，边的权值就是高度差的绝对值
# 将所有边按权值从小到大排序
# 每遍历一个边都把两边节点锁在的集合合并
# 当起点和终点合在一起了，这个遍历到的边就是答案
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        edges = []
        for i in range(row):
            for j in range(col):
                x = i * col + j
                if i > 0:
                    d = abs(heights[i][j] - heights[i - 1][j])
                    edges.append((d, x, x - col))
                if j > 0:
                    d = abs(heights[i][j] - heights[i][j - 1])
                    edges.append((d, x, x - 1))
        edges.sort(key=lambda e: e[0])

        def find(son: int) -> int:
            nonlocal p
            if p[son] != son:
                p[son] = find(p[son])
            return p[son]

        p = [i for i in range(col * row)]
        for d, x, y in edges:
            p[find(x)] = find(y)
            if find(0) == find(-1):  # 起点终点在一个连通块
                return d
        return 0  # 只有一个节点


# leetcode submit region end(Prohibit modification and deletion)

"""
[[1,2,2],[3,8,2],[5,3,5]]
[[1,2,3],[3,8,4],[5,3,5]]
[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
[[3]]
[[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
[[10,8],[10,8],[1,2],[10,3],[1,3],[6,3],[5,2]]
"""
