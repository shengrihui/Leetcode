# 2786 访问数组中的位置使分数最大
# https://leetcode.cn/problems/visit-array-positions-to-maximize-score/

# leetcode submit region begin(Prohibit modification and deletion)
# dfs(i,j) 在 [i,n-1] 中选一个子序列且要求第一个元素的奇偶性为 j
# j 是子序列第一个元素 % 2 的结果
# 如果 nums[i] 的奇偶性与 j 不一样
# 不符合要求，nums[i] 不选，返回 dfs(i+1,j)
# 如果 nums[i] 的奇偶性与 j 一样
# 一定要选 nums[i]，
# 然后在 [i+1,n-1] 中选一个子序列，第一个元素的奇偶性为 奇数/偶数 两种的最大值
"""
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            # 从下标 i 开始选一个子序列，且第一个元素的奇偶性为 j
            if i == len(nums):
                return 0
            if nums[i] % 2 != j:
                return dfs(i + 1, j)
            return nums[i] + max(dfs(i + 1, j), dfs(i + 1, j ^ 1) - x)

        return dfs(0, nums[0] % 2)
"""

"""
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            v = nums[i]
            r = v % 2
            f[i][r ^ 1] = f[i + 1][r ^ 1]
            f[i][r] = v + max(f[i + 1][r], f[i + 1][r ^ 1] - x)
        return f[0][nums[0] % 2]
"""


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        f = [0, 0]
        for v in reversed(nums):
            r = v % 2
            f[r] = max(f[r], f[r ^ 1] - x) + v
        return f[nums[0] % 2]

# leetcode submit region end(Prohibit modification and deletion)
