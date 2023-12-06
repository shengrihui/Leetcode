from typing import List
from collections import *
from itertools import *


# 题目：# 100076. 无限数组的最短子数组
# 题目链接：
# https://leetcode.cn/contest/weekly-contest-365/problems/minimum-size-subarray-in-infinite-array/
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)
        ans = target // s * n
        target %= s
        # print(s, ans, target)
        ans_add = 3 * n
        new_nums = nums[:] + nums[:]
        i, j = 0, 0
        s_t = new_nums[0]
        while j < 2 * n and i < 2 * n:
            while s_t < target and j < 2 * n - 1:
                j += 1
                s_t += new_nums[j]
            if j == 2 * n:
                break
            if s_t == target:
                ans_add = min(ans_add, j - i + 1)
                # print(i, j, ans_add,new_nums[i:j+1],sum(new_nums[i:j+1]))
            s_t -= new_nums[i]
            i += 1
        if ans_add == 3 * n:
            return -1
        return ans + ans_add


s = Solution()
examples = [
    (dict(nums=[1, 2, 3], target=5), 2),
    (dict(nums=[1, 1, 1, 2, 3], target=4), 2),
    (dict(nums=[2, 4, 6, 8], target=3), -1),
    (dict(nums=[17, 4, 3, 14, 17, 6, 15], target=85), -1),
    (dict(nums=[1, 4, 8, 5, 9, 8, 8, 2, 3, 1, 6, 2, 7, 5, 5, 3, 3, 5, 6], target=57), 10),
]
for e, a in examples:
    print(a, e)
    print(s.minSizeSubarray(**e))
