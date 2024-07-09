# 2369 检查数组是否存在有效划分
# https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int) -> int:
            res = False
            if i <= 0:
                return i < 0
            if i == 1:
                return nums[0] == nums[1]
            if nums[i] == nums[i - 1]:
                res |= dfs(i - 2)
            if nums[i] == nums[i - 1] == nums[i - 2] or nums[i] - 1 == nums[i - 1] and nums[i - 2] == nums[i] - 2:
                res |= dfs(i - 3)
            return res

        return dfs(len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)
