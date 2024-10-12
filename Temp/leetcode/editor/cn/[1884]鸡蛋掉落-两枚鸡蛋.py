# 1884 鸡蛋掉落-两枚鸡蛋
# https://leetcode.cn/problems/egg-drop-with-2-eggs-and-n-floors/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    @cache
    def twoEggDrop(self, n: int) -> int:
        if n == 0:  # 只有 0 层，答案是 0
            return 0
        # 从第 j 层落下第一个鸡蛋，
        #   如果碎了，接下来从 1 开始扔第二个鸡蛋，总操作为 1 + j - 1 = j
        #   如果没碎，问题变成 1 + dfs(n - j)
        # 两个情况取最大值，为了保证找到 f
        # 枚举 1 到 n 所有情况取最小值
        return min(max(j, self.twoEggDrop(n - j) + 1) for j in range(1, n + 1))


# f = [2000] * 1001
# f[0] = 0
# for i in range(1, 1001):
#     for j in range(1, i + 1):
#         f[i] = min(f[i], max(j, f[i - j] + 1))
f = [0] * 1001
for i in range(1, len(f)):
    f[i] = min(max(j, f[i - j] + 1) for j in range(1, i + 1))


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return f[n]


class Solution:
    def twoEggDrop(self, n: int) -> int:
        return ceil((sqrt(n * 8 + 1) - 1) / 2)
# leetcode submit region end(Prohibit modification and deletion)
