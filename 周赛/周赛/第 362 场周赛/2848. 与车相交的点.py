from itertools import accumulate
from typing import List
from collections import *


# 题目：# 2848. 与车相交的点
# 题目链接：https://leetcode.cn/problems/points-that-intersect-with-cars/

# class Solution:
#     def numberOfPoints(self, nums: List[List[int]]) -> int:
#         res = []
#         for s, e in nums:
#             res.extend(list(range(s, e + 1)))
#         return len(set(res))

# class Solution:
#     def numberOfPoints(self, nums: List[List[int]]) -> int:
#         res = set()
#         for s, e in nums:
#             res |= set(range(s, e + 1))
#         return len(res)

# 差分数组
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        diff = [0] * 102
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)
        for start, end in nums:
            # 区间 [start,end] 的值都加1
            # 差分数组修改 start和end+1
            # 对应差分数组的前缀和数组中大于0的位置就是有车的位置
            diff[start] += 1
            diff[end + 1] -= 1
        # ans = 0
        # pre = [0] * (max_end + 2)
        # for i, x in enumerate(diff[1:]):
        #     pre[i] = pre[i - 1] + diff[i]
        #     ans += pre[i] > 0
        # print(diff)
        # print(pre)
        # return ans
        return sum(x > 0 for x in accumulate(diff))


s = Solution()
examples = [
    (dict(nums=[[3, 6], [1, 5], [4, 7]]), 7),
    (dict(nums=[[1, 3], [5, 8]]), 7),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfPoints(**e))
