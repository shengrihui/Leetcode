from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd


# 题目：100168. 使数组异或和等于 K 的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-121/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
# 题库：https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        bits = [0] * 20
        for x in nums:
            for j in range(20):
                bits[j] += (x >> j) & 1
        k_bits = [(k >> j) & 1 for j in range(20)]
        return sum(x & 1 != y for x, y in zip(bits, k_bits))


s = Solution()
examples = [
    (dict(nums=[2, 1, 3, 4], k=1), 2),
    (dict(nums=[2, 0, 2, 0], k=0), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minOperations(**e))
