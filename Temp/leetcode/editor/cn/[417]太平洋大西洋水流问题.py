# 417 太平洋大西洋水流问题
# https://leetcode.cn/problems/pacific-atlantic-water-flow/


# leetcode submit region begin(Prohibit modification and deletion)
# 从太平洋或者大西洋的边上开始BFS
# 找到水能流到太平洋或者大西洋的位置集合
# 然后求两个的交集
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def find(a: List[[int, int]]) -> set:
            q = deque(a)
            vis = set(a)
            while q:
                i, j = q.popleft()
                for ni, nj in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in vis and heights[i][j] <= heights[ni][nj]:
                        q.append((ni, nj))
                        vis.add((ni, nj))
            return vis

        n, m = len(heights), len(heights[0])
        pacific = find([(i, 0) for i in range(n)] + [(0, j) for j in range(m)])  # 太平洋
        atlantic = find([(i, m - 1) for i in range(n)] + [(n - 1, j) for j in range(m)])  # 大西洋
        return list(map(list,pacific & atlantic))
# leetcode submit region end(Prohibit modification and deletion)
