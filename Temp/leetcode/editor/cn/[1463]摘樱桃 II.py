# 1463 摘樱桃 II
# https://leetcode.cn/problems/cherry-pickup-ii/


# leetcode submit region begin(Prohibit modification and deletion)

# https://leetcode.cn/problems/cherry-pickup-ii/solutions/2768158/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-i70v
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # f[i][j][k] 是从 (i,j) 和 (i,k) 出发到最后一行能得到的最大樱桃数
        # 所以答案是 f[0][1][n]
        # 最外层从后往前遍历
        # 这里用上了滚动数组
        pre = [[0] * (col + 2) for _ in range(row + 2)]
        cur = [[0] * (col + 2) for _ in range(row + 2)]
        # 遍历是用的是 grid 的下标，转换到 f 数组里都 +1
        # 所以 f 数组的列下标范围是 j,j+1,j+2
        for i in range(row - 1, -1, -1):
            for j in range(min(col, i + 1)):  # j 的最大值 min(i,col-1)
                for k in range(max(j + 1, col - 1 - i), col):  # 只考虑 k > j 的情况，所以最小值 max(j+1,col-1-i)
                    cur[j + 1][k + 1] = max(
                        pre[j][k], pre[j + 1][k], pre[j + 2][k],
                        pre[j][k + 1], pre[j + 1][k + 1], pre[j + 2][k + 1],
                        pre[j][k + 2], pre[j + 1][k + 2], pre[j + 2][k + 2],
                    ) + grid[i][j] + grid[i][k]
            pre, cur = cur, pre
        return pre[1][col]


"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            # 机器人 A 在(i,j)，机器人 B 在(i,k) 得到的樱桃最大值
            if i == row or j < 0 or j >= col or k < 0 or k >= col:
                return 0
            res = 0
            # 当前拿到的映泰
            val = grid[i][j] + (grid[i][k] if j != k else 0)
            for kk in (k - 1, k, k + 1):
                for jj in (j - 1, j, j + 1):
                    res = max(res, dfs(i + 1, jj, kk))
            return res + val

        return dfs(0, 0, col - 1)
"""
# leetcode submit region end(Prohibit modification and deletion)
