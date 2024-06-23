# 第 403 场周赛 第 1 题
# 题目：100342. 最小元素和最大元素的最小平均值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-403/problems/minimum-average-of-smallest-and-largest-elements/
# 题库：https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements

from math import inf
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = inf
        nums.sort()
        n = len(nums)
        for i in range(n // 2):
            a = (nums[i] + nums[n - 1 - i]) / 2
            ans = min(ans, a)
        return ans


s = Solution()
examples = [
    (dict(nums=[7, 8, 3, 4, 15, 13, 4, 1]), 5.5),
    (dict(nums=[1, 9, 8, 3, 10, 5]), 5.5),
    (dict(nums=[1, 2, 3, 7, 8, 9]), 5.0),
]
for e, a in examples:
    print(a, e)
    print(s.minimumAverage(**e))
