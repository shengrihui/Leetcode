# 611 有效三角形的个数
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()
        if n < 3 or nums[-1] == 0:
            return 0
        pos = 0
        while nums[pos] == 0:
            pos += 1
        for i in range(2, n):
            x = nums[i]
            l, r = pos, i - 1
            while l < r:
                if nums[l] + nums[r] > x:
                    ans += r - l  # **
                    r -= 1
                elif nums[l] + nums[r] <= x:
                    l += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
