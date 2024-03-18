# 第 387 场周赛 第 4 题
# 题目：100246. 将元素分配到两个数组中 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-387/problems/distribute-elements-into-two-arrays-ii/
# 题库：https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii

from typing import List
from collections import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, isqrt
import bisect
from bisect import *
from sortedcontainers import SortedList


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, sl1 = [nums[0]], SortedList([nums[0]])
        arr2, sl2 = [nums[1]], SortedList([nums[1]])
        for i in range(2, len(nums)):
            x = nums[i]
            gc1 = len(sl1) - sl1.bisect_right(x)
            gc2 = len(sl2) - sl2.bisect_right(x)
            if gc1 > gc2:
                arr1.append(x)
                sl1.add(x)
            elif gc2 > gc1:
                arr2.append(x)
                sl2.add(x)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(x)
                    sl1.add(x)
                else:
                    arr2.append(x)
                    sl2.add(x)
        return arr1 + arr2


s = Solution()
examples = [
    (dict(nums=[2, 1, 3, 3]), [2, 3, 1, 3]),
    (dict(nums=[5, 14, 3, 1, 2]), [5, 3, 1, 2, 14]),
    (dict(nums=[3, 3, 3, 3]), [3, 3, 3, 3]),
]
for e, a in examples:
    print(a, e)
    print(s.resultArray(**e))
