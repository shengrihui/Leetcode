# 2602 使数组元素全部相等的最少操作次数
# https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # return [sum(abs(x - q) for x in nums) for q in queries]
        nums.sort()
        n = len(nums)
        # 计算 nums[i] 到 nums[j] 的和（[i,j])
        # pre_sum[j+1] - pre_sum[i]
        # 或者说，pre_sum[j] - pre_sum[i] 是 nums[i:j] ([i,j)) 的和
        # 因为 pre_sum[i+1] = nums[0] + ... + nums[i]
        pre_sum = list(accumulate(nums, initial=0))
        ans = []
        for q in queries:
            # q 插入 nums 的位置，nums[:i] 都小于 q
            # 也就是 nums 中有 i 个数比 q 小
            i = bisect.bisect_left(nums, q)
            left = i * q - pre_sum[i]  # 前 i 个数都变成 q 的和 - 原来前 i 个数的和 = 前 i 个数变成 q 的操作次数
            # 操作之前 sum(nums[i:]) = pre_sum[n] - pre_sum[i]
            # 操作之后 有 n-i 个数
            right = pre_sum[n] - pre_sum[i] - q * (n - i)
            ans.append(left + right)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
