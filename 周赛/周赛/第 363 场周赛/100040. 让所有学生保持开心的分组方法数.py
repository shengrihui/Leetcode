from itertools import *
from typing import List


# 题目：# 100040. 让所有学生保持开心的分组方法数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-363/problems/happy-students/
# class Solution:
#     def countWays(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = 0
#         for i in range(1 << n):
#             bi = bin(i)[2:].rjust(n, "0")
#             choose = bi.count('1')
#             not_choose = n - choose
#             flag = True
#             for j, b in enumerate(bi):
#                 if b == "1":
#                     if choose > nums[j]:
#                         continue
#                     else:
#                         flag = False
#                         break
#                 if b == "0":
#                     if choose < nums[j]:
#                         continue
#                     else:
#                         flag = False
#                         break
#             if flag:
#                 ans += 1
#
#         return ans


class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # 如果最小不是0，那么可以有什么都不选着一种方案
        # 因为题目数据范围要求numsd的最大值不超过数组长度也就是总人数
        # 所有全部都选着一定是一种方案
        ans = nums[0] > 0 + 1
        for i, (x, y) in enumerate(pairwise(nums)):
            ans += x < i + 1 < y
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 1]), 2),
    (dict(nums=[6, 0, 3, 3, 6, 7, 2, 7]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.countWays(**e))
