from typing import List
from math import inf, gcd


# 题目：100157. 大于等于顺序前缀和的最小缺失整数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-121/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
# 题库：https://leetcode.cn/problems/smallest-missing-integer-greater-than-sequential-prefix-sum

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        pre_s = (nums[0] + nums[i - 1]) * (i - 0) // 2
        # pre_s = sum(nums[:i])
        while pre_s in nums:
            pre_s += 1
        return pre_s


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 2, 5]), 6),
    (dict(nums=[3, 4, 5, 1, 12, 14, 13]), 15),
    (dict(nums=[46, 8, 2, 4, 1, 4, 10, 2, 4, 10, 2, 5, 7, 3, 1]), 47),
]
for e, a in examples:
    print(a, e)
    print(s.missingInteger(**e))
