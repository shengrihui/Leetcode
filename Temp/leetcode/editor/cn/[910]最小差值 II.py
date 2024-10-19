# 910 最小差值 II
# https://leetcode.cn/problems/smallest-range-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/smallest-range-ii/solutions/2928780/xiao-de-bian-da-da-de-bian-xiao-pythonja-8fnp
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        a, b = nums[0] + k, nums[-1] - k
        # 贪心策略：小的变大，大的变小
        # 即 nums[:i] 变大，nums[i:] 变小
        # 最大值要么是 nums[-1] - k， 要么是 nums[i-1] + k
        # 最小值要么是 nums[0] + k， 要么是 nums[i] - k
        for x, y in pairwise(nums):
            mx = max(b, x + k)
            mn = min(a, y - k)
            ans = min(ans, mx - mn)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
