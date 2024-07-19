# 3095 或值至少 K 的最短子数组 I
# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = inf
        for i in range(n):
            t = nums[i]
            for j in range(i, n):
                t |= nums[j]
                if t >= k:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != inf else -1
# leetcode submit region end(Prohibit modification and deletion)
