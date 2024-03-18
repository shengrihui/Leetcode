from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100178. 将数组分成最小总代价的子数组 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-122/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
# 题库：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        t = sorted(enumerate(nums[1:dist + 2], 1), key=lambda x: x[1])
        print(t)
        # ans = nums[0] + sum(sorted(t)[:k])
        # mx, mxi = -1, -1
        # mn, mni = n, n
        # for i in range(1, dist + 1):
        #     if nums[i] > mx:
        #         mx = nums[i]
        #     if nums[i] >= mx:
        #         mxi = i
        #     if nums[i] < mn:
        #         mn = nums[i]
        #     if nums[i] <= mn:
        #         mni = i
        # for i in range(dist + 1, n):
        #     x = nums[i]
        #     if i - mxi > dist or x > mx:
        #         ans = ans - mx + x
        #         mx, mxi = x, i
        #     if i - mni > dist or x < mn:
        #         ans = ans - mn + x
        #         mn, mni = x, i
        # return ans


s = Solution()
examples = [
    (dict(nums=[1, 3, 2, 6, 4, 2], k=3, dist=3), 5),
    (dict(nums=[10, 1, 2, 2, 2, 1], k=4, dist=3), 15),
    (dict(nums=[10, 8, 18, 9], k=3, dist=1), 36),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
