from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf

# 题目：100136. 统计好分割方案的数目
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-375/problems/count-the-number-of-good-partitions/
# 题库：https://leetcode.cn/problems/count-the-number-of-good-partitions

MOD = 10 ** 9 + 7
# @cache
# def count(n: int) -> int:
#     if n == 1:
#         return 1
#     ans = 1
#     for i in range(1, n):
#         ans += count(i)
#     return ans % MOD

MX = 10 ** 5
# pre = [1] * (MX + 1)
# s = 0
# for i in range(1, MX + 1):
#     pre[i] += s
#     s = (s + pre[i]) % MOD
pre = [1] * (MX + 1)
for i in range(2, MX + 1):
    pre[i] = pre[i - 1] * 2 % MOD


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        rightest = defaultdict(int)
        for i, x in enumerate(nums):
            rightest[x] = i
        i = 0
        groups = 0
        n = len(nums)
        while i < n:
            r = rightest[nums[i]]
            while i <= r:
                r = min(n - 1, max(r, rightest[nums[i]]))
                i += 1
            groups += 1
        # return pow(2, groups - 1, MOD)
        return pre[groups] % MOD


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4]), 8),
    (dict(nums=[1, 1, 1, 1]), 1),
    (dict(nums=[1, 2, 1, 3]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfGoodPartitions(**e))
