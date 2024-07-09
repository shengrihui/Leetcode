# 2132 用邮票贴满网格图
# https://leetcode.cn/problems/stamping-the-grid/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        # 二维前缀和
        pre_sum = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            # for j in range(1, n + 1):
            #     pre_sum[i][j] = grid[i - 1][j - 1]+ pre_sum[i][j - 1]
            # for j in range(1, n + 1):
            #     pre_sum[i][j] +=   pre_sum[i - 1][j]
            for j in range(1, n + 1):
                pre_sum[i][j] = grid[i - 1][j - 1] + pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1]

        # 二维差分数组
        diff = [[0] * (n + 2) for _ in range(m + 2)]  # +2 是因为查分数组的“后面”还有有一个
        for i in range(stampHeight, m + 1):
            for j in range(stampWidth, n + 1):
                # 邮票的范围在 grid 中 [ii-1,i-1] [jj-1,j-1]
                #         在 pre_sum 和 diff 中 [ii,i] [jj,j]
                ii, jj = i - stampHeight + 1, j - stampWidth + 1
                if pre_sum[i][j] - pre_sum[ii - 1][j] - pre_sum[i][jj - 1] + pre_sum[ii - 1][jj - 1] == 0:  # 放一张邮票
                    diff[ii][jj] += 1
                    diff[i + 1][jj] -= 1
                    diff[ii][j + 1] -= 1
                    diff[i + 1][j + 1] += 1
        # 检查
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算差分数组的前缀和 -> (i,j) 上放了多少张邮票，原地
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                # 原来的空的，但后来没有邮票
                if grid[i - 1][j - 1] == 0 and diff[i][j] == 0:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

"""
[
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,1,0,0],
[0,0,0,0,1],
[0,0,0,1,1]]
"""
