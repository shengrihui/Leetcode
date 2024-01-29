from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, isqrt, sqrt


# 题目：100206. 子集中元素的最大数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-382/problems/find-the-maximum-number-of-elements-in-subset/
# 题库：https://leetcode.cn/problems/find-the-maximum-number-of-elements-in-subset

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1
        for x in sorted(cnt, reverse=True):
            c = 1
            while True and x != 1:
                y = isqrt(x)
                if cnt[y] > 1 and y == sqrt(x):
                    c += 1
                    x = y
                else:
                    break
            ans = max(c, ans)
        return max(cnt[1] - (cnt[1] % 2 == 0), ans * 2 - 1)


"""
# 灵神
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = cnt[1] - (cnt[1] % 2 ^ 1)
        del cnt[1]
        for x in cnt:
            res = 0
            while cnt[x] > 1:
                res += 2
                x *= x
            ans = max(ans, res + (1 if x in cnt else -1))  # 保证 res 是奇数
        return ans
"""

s = Solution()
examples = [
    (dict(nums=[5, 4, 1, 2, 2]), 3),
    (dict(nums=[1, 3, 2, 4]), 1),
    (dict(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]), 9),
]
for e, a in examples:
    print(a, e)
    print(s.maximumLength(**e))
