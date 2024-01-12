from typing import List


# 题目：# 100019. 将数组分割成最多数目的子数组
# 题目链接：
# https://leetcode.cn/contest/biweekly-contest-114/problems/split-array-into-maximum-number-of-subarrays/
# https://leetcode.cn/problems/split-array-into-maximum-number-of-subarrays/
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        r = nums[0]
        for x in nums:
            r &= x
            if r == 0:
                break
        if r != 0:
            return 1
        ans = 0
        t = nums[0]
        i = 0
        while i < len(nums):
            t &= nums[i]
            if t == 0:
                ans += 1
                if i + 1 < len(nums):
                    t = nums[i + 1]
                i += 1
            else:
                i += 1
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 0, 2, 0, 1, 2]), 3),
    (dict(nums=[5, 7, 1, 3]), 1),
    (dict(nums=[1, 2, 2, 1]), 2),
    (dict(nums=[0, 0]), 2),
    (dict(nums=[0]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.maxSubarrays(**e))
