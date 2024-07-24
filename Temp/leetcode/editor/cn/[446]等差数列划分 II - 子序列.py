# 446 等差数列划分 II - 子序列
# https://leetcode.cn/problems/arithmetic-slices-ii-subsequence/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

# dfs(j,d) 以 nums[j] 结尾每两个相邻元素差为 d 的子序列的个数
# g[i][d] = [j1,j2,j3...] nums[i] - nums[j] = d
# dfs 中为什么是 1 + dfs(j,d)
# 那个 1 是 [nums[k],nums[j]]
# 而 dfs(k,d) 是 [...,nums[k],nums[j]] 的个数
# 因子子序最少 3 个元素，所以 i 和 j 循环那儿是 ans += dfs(j,d)
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        @cache
        def dfs(j: int, d: int) -> int:
            res = 0
            for k in g[i][d]:
                res += 1 + dfs(k, d)
            return res

        n = len(nums)
        if n < 3:
            return 0
        g = [defaultdict(list) for _ in range(n)]
        for i, x in enumerate(nums):
            for j in range(i + 1, n):
                g[j][nums[j] - x].append(i)
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, 0, -1):
                ans += dfs(j, nums[i] - nums[j])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
