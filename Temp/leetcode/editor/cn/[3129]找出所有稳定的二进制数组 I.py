# 3129 找出所有稳定的二进制数组 I
# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-i/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # 还有 i 个 0 j 个 1 ，在 i+j 的位置填 k
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if j < 0 or i < 0:
                return 0
            if i == 0:  # 没有 0 可以填了，剩下全部填 1
                return k == 1 and j <= limit
            if j == 0:
                return k == 0 and i <= limit
            if k == 0:  # 加上前一位填 0 或者 1，减去最后 limit 个0
                # 因为这一位是 0，所以都是 i-1
                return (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1)) % MOD
            return (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0)) % MOD

        MOD = 1_000_000_007
        ans = (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
        dfs.cache_clear()
        return ans
# leetcode submit region end(Prohibit modification and deletion)
