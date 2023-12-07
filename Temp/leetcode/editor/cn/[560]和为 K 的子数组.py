# 560 和为 K 的子数组
from collections import *
from typing import *


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         ans = 0
#         n = len(nums)
#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s += nums[j]
#                 if s == k:
#                     ans += 1
#
#         return ans

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        ans = 0
        pre = 0
        for x in nums:
            pre += x
            ans += mp[pre - k]
            mp[pre] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# print(s.subarraySum([1, 1, 1], 2))
# print(s.subarraySum([1, 2, 3], 3))
# print(s.subarraySum([1], 1))
print(s.subarraySum([1], 0))
