# 2765 最长交替子数组
# https://leetcode.cn/problems/longest-alternating-subarray/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = ans = 0
        while i < n:
            st = i
            i += 1
            while i < n and nums[i] - nums[st] == (i - st) % 2:
                i += 1
            ans = max(ans, i - st)
            if i < n - 1:
                i = max(st + 1, i - 1)
        return ans if ans > 1 else -1
# class Solution:
#     def alternatingSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         length = n
#         while length > 1:
#             for i in range(n - length + 1):
#                 s = nums[i:i + length]
#                 if s[0] + 1 != s[1]: continue
#                 for j in range(length):
#                     if s[j] - s[0] != j % 2:
#                         break
#                 else:
#                     return length
#             length -= 1
#         return -1
# leetcode submit region end(Prohibit modification and deletion)
