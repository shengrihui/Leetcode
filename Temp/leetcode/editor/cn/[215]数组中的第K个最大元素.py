# 215 数组中的第K个最大元素
# https://leetcode.cn/problems/kth-largest-element-in-an-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# 桶排序 / 计数排序
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n, mn, mx = len(nums), min(nums), max(nums)
        a = [0] * (mx - mn + 1)
        for x in nums:
            a[x - mn] += 1
        i = mx - mn
        while k > a[i]:
            k -= a[i]
            i -= 1
        return i + mn
# leetcode submit region end(Prohibit modification and deletion)
