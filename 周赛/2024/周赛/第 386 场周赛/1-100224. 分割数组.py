# 第 386 场周赛 第 1 题
# 题目：100224. 分割数组
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-386/problems/split-the-array/
# 题库：https://leetcode.cn/problems/split-the-array

from collections import *
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for v in cnt.values():
            if v > 2:
                return False
        return True


s = Solution()
examples = [
    (dict(nums=[1, 1, 2, 2, 3, 4]), True),
    (dict(nums=[1, 1, 1, 1]), False),
    (dict(nums=[6, 1, 3, 1, 1, 8, 9, 2]), False),
]
for e, a in examples:
    print(a, e)
    print(s.isPossibleToSplit(**e))
