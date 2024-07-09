# 312 戳气球
# https://leetcode.cn/problems/burst-balloons/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        val = [1] + nums + [1]

        # @lru_cache(None)
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= j - 1:
                return 0
            best = 0
            for m in range(i + 1, j):
                t = val[i] * val[m] * val[j]
                s = dfs(i, m) + dfs(m, j)
                best = max(best, s + t)
            return best

        return dfs(0, len(val) - 1)
# leetcode submit region end(Prohibit modification and deletion)
