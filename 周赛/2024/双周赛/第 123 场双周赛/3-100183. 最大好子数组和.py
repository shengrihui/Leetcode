# 第 123 场双周赛 第 3 题
# 题目：100183. 最大好子数组和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-123/problems/maximum-good-subarray-sum/
# 题库：https://leetcode.cn/problems/maximum-good-subarray-sum
import bisect
from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt

# 算出前缀和，记录每种值的下标
# 遍历数组的每一个元素作为子数组的第一个元素
# 枚举最后一个元素的下标，计算子数组的和，更新答案
# 超时
"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        ans = -inf
        for i, x in enumerate(nums):
            for y in [x + k, x - k]:
                for jj in range(len(d[y]) - 1, bisect.bisect_left(d[y], i) - 1, -1):
                    j = d[y][jj]
                    ans = max(ans, s[j + 1] - s[i])
        return ans if ans != -inf else 0
"""


# 小羊
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: inf)
        acc = 0  # 前缀和
        ans = -inf
        for num in nums:
            # d[num +/- k] = 以 num +/- k 为第一个元素的最小前缀和
            # 不包括 num +/- k 这个值
            # 所以要先更新 d[num] 再 更新 acc
            if num - k in d:
                ans = max(acc + num - d[num - k], ans)
            if num + k in d:
                ans = max(acc + num - d[num + k], ans)
            d[num] = min(d[num], acc)
            acc += num
        return ans if ans > -inf else 0


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5, 6], k=1), 11),
    (dict(nums=[-1, 3, 2, 4, 5], k=3), 11),
    (dict(nums=[-1, -2, -3, -4], k=2), -6),
]
for e, a in examples:
    print(a, e)
    print(s.maximumSubarraySum(**e))
