import itertools
from math import isqrt
from typing import List
from collections import *
from itertools import *

# 题目：# 2862. 完全子集的最大元素和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-363/problems/maximum-element-sum-of-a-complete-subset-of-indices/
# 题库：https://leetcode.cn/problems/maximum-element-sum-of-a-complete-subset-of-indices/description/

"""
记 core(n) 表示，n 去掉所有平方因子后的值
例如：
core(8) = 8/4 = 2
core(75)= 75/25 = 3
core(9) = core(4) = 1

题目要求的是，由下标组成的完全集，并这些下标对应的值的和最大。
这个集合肯定越大越好；
怎么让集合中的元素两辆相乘是个平方数呢？
该集合中的元素的 core(n) 一样。

方法一：
遍历 core(n) 的情况
for i in range(1,len(nums)+1) 因为len(nums)可能是个质数，所以包括它
枚举所有 core(i*j*j) = i 的下标，计算元素值的和
更新答案

方法二
计算每个下标的 core(i)

"""


# class Solution:
#     def maximumSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = 0
#         for i in range(1, n + 1):
#             s = 0
#             j = 1
#             while i * j * j <= n:
#                 s += nums[i * j * j - 1]
#                 j += 1
#             ans = max(ans, s)
#         return ans

def core(x):
    res = 1
    for i in range(2, isqrt(x) + 1):  # math.isqrt
        e = 0  # x里面有几个i
        while x % i == 0:  # i是x的因子，除掉它
            e += 1
            x //= i
        if e % 2 == 1:  # x里面有奇数个i
            res *= i
    if x > 1:  # x本身就是质数
        res *= x
    return res


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0 for _ in range(n + 1)]
        for i, x in enumerate(nums):
            s[core(i + 1)] += x
        return max(s)


s = Solution()
examples = [
    (dict(nums=[8, 7, 3, 5, 7, 2, 4, 9]), 16),
    (dict(nums=[5, 10, 3, 10, 1, 13, 7, 9, 4]), 19),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSum(**e))
