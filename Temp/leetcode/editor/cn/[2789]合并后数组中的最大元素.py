# 2789 合并后数组中的最大元素
# https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nums[i] += nums[i + 1]
        return nums[0]

# leetcode submit region end(Prohibit modification and deletion)
