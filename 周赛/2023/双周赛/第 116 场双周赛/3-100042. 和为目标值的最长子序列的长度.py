from typing import List


# 题目：100042. 和为目标值的最长子序列的长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-116/problems/length-of-the-longest-subsequence-that-sums-to-target/
# https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/

# class Solution:
#     def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         dp = [-1] * (target + 1)
#         dp[0] = 0
#         for x in nums:
#             if x > target:
#                 break
#             for i in range(target - x, -1, -1):
#                 if dp[i] >= 0:
#                     dp[i + x] = max(dp[i] + 1, dp[i + x])
#         return dp[target]

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # dp[i]：取多少数和为i
        dp = [-1] * (target + 1)
        dp[0] = 0
        for x in nums:
            for i in range(target - x, -1, -1):
                # dp[i]不是-1，那么 i + x 可以由 i 加上 x 得到
                # dp[i]  是-1，说明 i 都还没加到，i + x 就更加不到了
                # 也就是 dp[i + x] = max(dp[i] + 1, dp[i + x])
                if dp[i] >= 0 and dp[i] + 1 > dp[i + x]:
                    dp[i + x] = dp[i] + 1
        return dp[target]


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 5], target=9), 3),
    (dict(nums=[4, 1, 3, 2, 1, 5], target=7), 4),
    (dict(nums=[1, 1, 5, 4, 5], target=3), -1),
    (dict(nums=[1], target=1), 1),
    (dict(nums=[1, 1, 1, 1], target=4), 4),
    (dict(nums=[2, 13, 7, 3, 14, 8, 11, 10, 7, 13], target=44), 6),

]
for e, a in examples:
    print(a, e)
    print(s.lengthOfLongestSubsequence(**e))
