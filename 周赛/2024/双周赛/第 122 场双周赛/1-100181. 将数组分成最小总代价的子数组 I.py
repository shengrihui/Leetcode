from heapq import nsmallest
from typing import List


# 题目：100181. 将数组分成最小总代价的子数组 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-122/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
# 题库：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # num = sorted(nums[1:])
        # return nums[0] + num[0] + num[1]
        return nums[0] + sum(nsmallest(2, nums[1:]))


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 12]), 6),
    (dict(nums=[5, 4, 3]), 12),
    (dict(nums=[10, 3, 1, 1]), 12),
]
for e, a in examples:
    print(a, e)
    print(s.minimumCost(**e))
