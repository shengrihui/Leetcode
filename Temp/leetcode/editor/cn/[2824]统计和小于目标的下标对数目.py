# 2824 统计和小于目标的下标对数目
from typing import *


# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         return sum(nums[i] + nums[j] < target for i in range(len(nums)) for j in range(i + 1, len(nums)))

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 0, -1):
            x = nums[i]
            l, r = 0, i - 1
            while l <= r:
                mid = (l + r) // 2
                if x + nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            ans += r + 1
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            s = nums[i] + nums[j]
            if s < target:
                ans += j - i
                i += 1
            else:
                j -= 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
