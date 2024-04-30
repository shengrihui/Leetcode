# 第 395 场周赛 第 4 题
# 题目：100257. 找出唯一性数组的中位数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-395/problems/find-the-median-of-the-uniqueness-array/
# 题库：https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array

from collections import *
from typing import List

"""
数组长度 n
一共有 nn = n * (n+1) // 2 个非空子数组
中位数下标 m = (nn-1) // 2
要求的是第 k = m + 1 = (nn+1) // 2 大的数

check 
distinct 值小于 upper（二分答案） 的数组的数量是否小于 k
滑窗
distinct值=len(freq)
"""


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2

        def check(upper: int) -> bool:
            freq = Counter()
            cnt = l = 0  # 符合条件（distinct值小于upper)的子数组数量，窗口的左端点
            for r, in_ in enumerate(nums):
                freq[in_] += 1
                while len(freq) > upper:
                    out = nums[l]
                    freq[out] -= 1
                    if freq[out] == 0:
                        del freq[out]
                    l += 1
                cnt += r - l + 1  # 右端点为 r 左端点为 [l....r] 的子数组的 distinct 值都小于 k ，数量有 r - l + 1 个
                if cnt >= k:
                    return False
            return True

        left, right = 1, len(set(nums))
        while left <= right:
            upper = (left + right) // 2
            if check(upper):
                left = upper + 1
            else:
                right = upper - 1
        return left


s = Solution()
examples = [
    (dict(nums=[1, 2, 3]), 1),
    (dict(nums=[3, 4, 3, 4, 5]), 2),
    (dict(nums=[4, 3, 5, 4]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.medianOfUniquenessArray(**e))
