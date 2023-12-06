from typing import List


# 题目：# 6989. 几乎唯一子数组的最大和
# 题目链接： https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            # print(sub)
            if len(set(sub)) >= m:
                if sum(sub) > ans:
                    ans = sum(sub)
        return ans


s = Solution()
examples = [
    (dict(nums=[2, 6, 7, 3, 1, 7], m=3, k=4), 18),
    (dict(nums=[5, 9, 9, 2, 4, 5, 4], m=1, k=3), 23),
    (dict(nums=[1, 2, 1, 2, 1, 2, 1], m=3, k=3), 0),
]
for e, a in examples:
    print(e, a)
    print(s.maxSum(**e))
