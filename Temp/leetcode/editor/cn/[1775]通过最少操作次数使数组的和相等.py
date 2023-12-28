# 1775 通过最少操作次数使数组的和相等
# https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def help(s: List[int], b: List[int], diff: int) -> int:
            # 和小的数组 s ，大的 b
            res = 0
            for i in range(1, 6):  # 将 s 的 i 变 6，b 的 7-i 变 1 能是两个相等
                c = s[i] + b[7 - i]
                d = 6 - i  # 操作的改变两
                if c * d >= diff:
                    return res + diff // d + (diff % d != 0)  # 每一步的操作变化是 6-i
                res += c
                diff -= c * d
            return -1

        n, m = len(nums1), len(nums2)
        if 6 * n < m or 6 * m < n:  # 其中一个全是 6 了仍然比另一个全是 1 要小 -> 不能变过去
            return -1
        h1, h2 = [0] * 7, [0] * 7
        diff = 0  # 计算 sum(nums1) - sum(nums2)
        for i in nums1:
            h1[i] += 1
            diff += i
        for i in nums2:
            h2[i] += 1
            diff -= i
        if diff == 0:
            return 0
        if diff > 0:  # nums1 的和大
            return help(h2, h1, diff)
        return help(h1, h2, -diff)


# leetcode submit region end(Prohibit modification and deletion)

"""
[5,6,4,3,1,2]
[6,3,3,1,4,5,3,4,1,3,4]
[5,2,1,5,2,2,2,2,4,3,3,5]
[1,4,5,5,6,3,1,3,3]
[1,5,5,2,1,1,1,1,4,4,4,1,5,2,2,4,6,5,1,5,3,5,6,2,3,1,5,4,4,1,2,4,1,1,6,3,6,4,4,4,3,5,5,5,2,6,4,2,5,4,2,6,3,4,6,1,5,3,2,3,5,2,1,3,2,4,4,4,5,3,5,5,4,1,1,6,5,6,3,5,3,6,5,6,5,4,4,4,5,6,6,6,4,2,4,6,1,2,1,5,3,4,5,5,6,6,1,4,3,1,5,3,4,1,2,1,4,4,5,6,5,3,1,5,1,3,3,6,5,3,5,6,2,6,3,1,2,3,3,1,1,4,3,2,6,6,2,1,2,4,3,5,5,4,3,1,1,5,2,5,1,4,5,6,4,5,2,1,2,5,3,2,6,3,4,3,4,5,4,6,3,4,4,3,3,4,2,2,6,2,6,3,1,1,5,3,1,1,4,2,5,5,5,4,3,6,5,5,5,1,1,3,6,2,3,6,3,4,2,5,4,4,3,5,6,4,3,5,1,1,3,3,1,1,6,4,6,2,1,4,3,5,5]
[1,2,5,4,3,3,5,1,1,6,2,5,4,4,5,6,6,4,2,5,6,2,3,4,5,2,4,4,3,6,6,5,4,1,2,1,2,3,3,2,6,1,1,1,1,3,5,6,2,1,1,1,4,6,5]
"""
