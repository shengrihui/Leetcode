# 3097 或值至少为 K 的最短子数组 II
# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            if x >= k:
                return 1
            for j in range(i - 1, -1, -1):
                if nums[j] | x == nums[j]:
                    break
                nums[j] |= x
                if nums[j] >= k:
                    ans = min(ans, i - j + 1)
                    break
        return ans if ans != inf else -1
# leetcode submit region end(Prohibit modification and deletion)
