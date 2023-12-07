# 18 四数之和
from typing import *


# 丑陋的暴力，超时了
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#       n = len(nums)
#         mapping = {v: i for i, v in enumerate(sorted(set(nums)))}
#         ans = []
#         seen = set()
#         for a in range(n - 3):
#             for b in range(a + 1, n - 2):
#                 for c in range(b + 1, n - 1):
#                     for d in range(c + 1, n):
#                         aa, bb, cc, dd = nums[a], nums[b], nums[c], nums[d]
#                         t = 0
#                         for i, tt in enumerate(sorted([aa, bb, cc, dd])):
#                             t |= mapping[tt] << (i * 8)
#                         if t not in seen:
#                             seen.add(t)
#                             if aa + bb + cc + dd == target:
#                                 ans.append([aa, bb, cc, dd])
#         return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        last2 = nums[-1] + nums[-2]
        last3 = last2 + nums[-3]
        for a in range(n - 3):
            aa = nums[a]
            if a and aa == nums[a - 1] or aa + last3 < target:
                continue
            if aa + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            for b in range(a + 1, n - 2):
                bb = nums[b]
                if b != a + 1 and bb == nums[b - 1] or aa + bb + last2 < target:
                    continue
                if aa + bb + nums[b + 1] + nums[b + 2] > target:
                    break
                c, d = b + 1, n - 1
                while c < d:
                    s = aa + bb + nums[c] + nums[d]
                    if s == target:
                        ans.append([aa, bb, nums[c], nums[d]])
                    if s >= target:
                        d -= 1
                        while d > c and nums[d] == nums[d + 1]:
                            d -= 1
                    if s <= target:
                        c += 1
                        while d > c and nums[c] == nums[c - 1]:
                            c += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
