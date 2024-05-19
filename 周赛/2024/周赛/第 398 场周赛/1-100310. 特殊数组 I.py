# 第 398 场周赛 第 1 题
# 题目：100310. 特殊数组 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-398/problems/special-array-i/
# 题库：https://leetcode.cn/problems/special-array-i

from itertools import *
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(x % 2 != y % 2 for x, y in pairwise(nums))


s = Solution()
examples = [
    (dict(nums=[1]), True),
    (dict(nums=[2, 1, 4]), True),
    (dict(nums=[4, 3, 1, 6]), False),
]
for e, a in examples:
    print(a, e)
    print(s.isArraySpecial(**e))
