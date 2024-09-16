# 第 415 场周赛 第 1 题
# 题目：100434. 数字小镇中的捣蛋鬼
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-415/problems/the-two-sneaky-numbers-of-digitville/
# 题库：https://leetcode.cn/problems/the-two-sneaky-numbers-of-digitville

from collections import Counter
from math import isqrt
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [x for x in cnt if cnt[x] > 1]


# O(1) 空间
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = s2 = 0
        n = len(nums) - 2
        for i in range(n):
            s += nums[i] - i
            s2 += nums[i] * nums[i] - i * i
        s += nums[-1] + nums[-2]
        s2 += nums[-1] * nums[-1] + nums[-2] * nums[-2]
        # s = x + y, s2 = x^2 + y^2
        # x^2 + s^2 - 2*s*x + x^2 = s2
        x = (2 * s + isqrt(4 * s * s - 4 * 2 * (s * s - s2))) // 4
        return [x, s - x]


s = Solution()
examples = [
    (dict(nums=[0, 1, 1, 0]), [0, 1]),
    (dict(nums=[0, 3, 2, 1, 3, 2]), [2, 3]),
    (dict(nums=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]), [4, 5]),
]
for e, a in examples:
    print(a, e)
    print(s.getSneakyNumbers(**e))
