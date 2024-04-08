# 2009 使数组连续的最少操作数
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(set(nums))
        ans = left = 0
        for i, x in enumerate(a):
            # 正难则反，考虑最后有多少留下
            # x 作为右端点（最大值）
            # 移动左端点 left ，使最小值在 [ x-n+1 ,x ] 内
            while a[left] < x - n + 1:
                left += 1
            ans = max(ans, i - left + 1)
        return n - ans
# leetcode submit region end(Prohibit modification and deletion)
