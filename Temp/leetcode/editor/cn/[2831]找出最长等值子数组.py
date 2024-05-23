# 2831 找出最长等值子数组
# https://leetcode.cn/problems/find-the-longest-equal-subarray/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        ans = 0
        for x in d:
            d[x].sort()
            delete = 0
            left = 0
            for right, r_i in enumerate(d[x]):
                if right > 0:
                    delete += d[x][right] - d[x][right - 1] - 1
                while left < right and delete > k:
                    left += 1
                    delete -= d[x][left] - d[x][left - 1] - 1
                ans = max(ans, right - left + 1)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)
