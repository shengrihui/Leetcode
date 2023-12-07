from typing import List


# 题目：100135. 找到最大非递减数组的长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-118/problems/find-maximum-non-decreasing-array-length/
# 题库：https://leetcode.cn/problems/find-maximum-non-decreasing-array-length

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        pass


s = Solution()
examples = [
    (dict(nums=[5, 2, 2]), 1),
    (dict(nums=[1, 2, 3, 4]), 4),
    (dict(nums=[4, 3, 2, 6]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.findMaximumLength(**e))
