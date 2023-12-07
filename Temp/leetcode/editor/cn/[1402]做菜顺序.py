# 1402 做菜顺序
from typing import *


# # [-1,-8,0,5,-9]
# # [5,0,-1,-8,-9]
# # ans = 0
# # [5]         ans = 5*1                 = 5  = ans + sum([5])
# # [5,0]       ans = 5*2+0*1             = 10 = ans + sum([5,0])
# # [5,0,-1]    ans = 5*3+0*2+(-1)        = 14 = ans + sum([5,0,-1])
# # [5,0,-1,-8] ans = 5*4+0*3+(-1)*2+(-8) = 10 = ans + sum([5,0,-1,-8])
# # 也就是 sum([...]) 是个正数，选s[i]
# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort(key=lambda x: -x)
#         ans = presum = 0
#         for s in satisfaction:
#             if presum + s > 0:
#                 presum += s
#                 ans += presum
#             else:
#                 break
#         return ans


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        n = len(satisfaction)
        # 前i个菜中选择j个菜的最大满意度
        # 因此i>=j
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j - 1] + satisfaction[i - 1] * j  # 选择第i个菜，它是第j个做的
                if j < i:  # j==i的时候不能走这一步是因为dp[i-1][i]=0,那些负数的都会因为max变成0
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])  # 不选第i个菜，那就是在前i-i个菜中选j个菜。
        return max(dp[-1])

# leetcode submit region end(Prohibit modification and deletion)
