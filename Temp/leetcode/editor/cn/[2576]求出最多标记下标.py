# 2576 求出最多标记下标
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/solutions/2134078/er-fen-da-an-pythonjavacgo-by-endlessche-t9f5
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums[(len(nums) + 1) // 2:]:
            if nums[i] * 2 <= x:
                i += 1
        return i * 2


# 二分开区间
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) // 2 + 1
        while left + 1 < right:
            k = (left + right) // 2
            # 最大最小 k 个配对
            # n - k + i -> i - k
            if all(nums[i] * 2 <= nums[i - k] for i in range(k)):
                left = k
            else:
                right = k
        return left * 2

# leetcode submit region end(Prohibit modification and deletion)
