# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:48:34 2021

@author: 11200
"""

from collections import defaultdict
from functools import cache


# dfs(j,d) 以 nums[j] 结尾每两个相邻元素差为 d 的子序列的个数
# g[i][d] = [j1,j2,j3...] nums[i] - nums[j] = d
# dfs 中为什么是 1 + dfs(j,d)
# 那个 1 是 [nums[k],nums[j]]
# 而 dfs(k,d) 是 [...,nums[k],nums[j]] 的个数
# 因子子序最少 3 个元素，所以 i 和 j 循环那儿是 ans += dfs(j,d)
def numberOfArithmeticSlices(nums):
    @cache
    def dfs(i: int, d: int) -> int:
        res = 0
        for j in g[i][d]:
            res += 1 + dfs(j, d)
        return res

    n = len(nums)
    if n < 3:
        return 0
    g = [defaultdict(list) for _ in range(n)]
    for i, x in enumerate(nums):
        for j in range(i + 1, n):
            g[j][nums[j] - x].append(i)
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, 0, -1):
            ans += dfs(j, nums[i] - nums[j])
    return ans


print(7, numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
print(16, numberOfArithmeticSlices(nums=[7, 7, 7, 7, 7]))
print(3, numberOfArithmeticSlices(nums=[3, -1, -5, -9]))
print(2, numberOfArithmeticSlices(nums=[2, 2, 3, 4]))
print(4, numberOfArithmeticSlices(nums=[0, 1, 2, 2, 2, ]))

"""
446. 等差数列划分 II - 子序列
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

 

示例 1：

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
示例 2：

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。
 

提示：

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1

"""
