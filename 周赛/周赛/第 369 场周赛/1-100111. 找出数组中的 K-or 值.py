from typing import List
from collections import *
from itertools import *
from math import *


# 题目：100111. 找出数组中的 K-or 值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-369/problems/find-the-k-or-of-an-array/

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = [0] * 32
        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    cnt[i] += 1
        ans = 0
        for i in range(32):
            if cnt[i] >= k:
                ans += 2 ** i
        return ans


s = Solution()
examples = [
    (dict(nums=[7, 12, 9, 8, 9, 15], k=4), 9),
    (dict(nums=[2, 12, 1, 11, 4, 5], k=6), 0),
    (dict(nums=[10, 8, 5, 9, 11, 6, 8], k=1), 15),
]
for e, a in examples:
    print(a, e)
    print(s.findKOr(**e))
