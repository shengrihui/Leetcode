# 第 393 场周赛 第 2 题
# 题目：100265. 素数的最大距离
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-393/problems/maximum-prime-difference/
# 题库：https://leetcode.cn/problems/maximum-prime-difference

from math import isqrt
from typing import List


def isprime(x):
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True


prime = set(i for i in range(2, 98) if isprime(i))


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = 0, n - 1
        while nums[a] not in prime:
            a += 1
        while nums[b] not in prime:
            b -= 1
        return b - a


s = Solution()
examples = [
    (dict(nums=[4, 2, 9, 5, 3]), 3),
    (dict(nums=[4, 8, 2, 8]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.maximumPrimeDifference(**e))
