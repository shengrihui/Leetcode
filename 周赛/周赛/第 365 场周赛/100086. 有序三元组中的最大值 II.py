from typing import List
from collections import *
from itertools import *


# 题目：# 100086. 有序三元组中的最大值 II
# 题目链接：
# https://leetcode.cn/contest/weekly-contest-365/problems/maximum-value-of-an-ordered-triplet-ii/
# 题目：# 100088. 有序三元组中的最大值 I
# 题目链接：
# https://leetcode.cn/contest/weekly-contest-365/problems/maximum-value-of-an-ordered-triplet-i/


# class Solution:
#     def maximumTripletValue(self, nums: List[int]) -> int:
#         inf = 10 ** 7
#         n = len(nums)
#         right_max = [0] * n
#         right_max[-1] = nums[-1]
#         right_max[-2] = max(nums[-1], nums[-2])
#         right_min = [[inf, -1]] * n
#         # right_min[-1] = [nums[-1], n - 1]
#         right_min[-2] = [nums[-2], n - 2]
#         for i in range(n - 3, -1, -1):
#             right_max[i] = max(right_max[i + 1], nums[i])
#             if right_min[i + 1][0] < nums[i]:
#                 right_min[i] = right_min[i + 1]
#             else:
#                 right_min[i] = [nums[i], i]
#         print(right_max)
#         print(right_min)
#         ans = 0
#         for i, x in enumerate(nums):
#             if i == n - 2:
#                 break
#             y, y_i = right_min[i + 1]
#             z = right_max[y_i + 1]
#             # print(x, y, z, y_i)
#             ans = max((x - y) * z, ans)
#         return max(ans, 0)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n
        right_max = [0] * n
        left_max[1] = nums[0]
        right_max[-2] = nums[-1]
        for i in range(2, n):
            left_max[i] = max(nums[i - 1], left_max[i - 1])
            right_max[-i - 1] = max(nums[-i], right_max[-i])
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, (left_max[i] - nums[i]) * right_max[i])
        return ans


s = Solution()
examples = [
    (dict(nums=[12, 6, 1, 2, 7]), 77),
    (dict(nums=[1, 2, 3]), 0),
    (dict(nums=[2, 3, 1]), 0),
    (dict(nums=[15, 3, 3, 18, 19, 13, 7, 5, 18, 1, 8, 5]), 252),
]
for e, a in examples:
    print(a, e)
    print(s.maximumTripletValue(**e))
