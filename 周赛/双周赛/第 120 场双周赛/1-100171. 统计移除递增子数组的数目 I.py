from typing import List
from math import inf


# 题目：100171. 统计移除递增子数组的数目 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-120/problems/count-the-number-of-incremovable-subarrays-i/
# 题库：https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i

# 暴力枚举所有区间
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def f(s):
            for i in range(1, len(s)):
                if s[i] <= s[i - 1]:
                    return False
            return True

        if f(nums):
            return len(nums) * (len(nums) + 1) // 2
        nums.append(inf)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                sub = nums[:i] + nums[j:]
                ans += f(sub)
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4]), 10),
    (dict(nums=[6, 5, 7, 8]), 7),
    (dict(nums=[8, 7, 6, 6]), 3),
]
for e, a in examples:
    print(a, e)
    print(s.incremovableSubarrayCount(**e))
