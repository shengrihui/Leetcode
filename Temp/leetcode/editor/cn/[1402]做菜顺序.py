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


# 一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。 
# 
#  一道菜的 「 like-time 系数 」定义为烹饪这道菜结束的时间（包含之前每道菜所花费的时间）乘以这道菜的满意程度，也就是 time[i]*
# satisfaction[i] 。 
# 
#  返回厨师在准备了一定数量的菜肴后可以获得的最大 like-time 系数 总和。 
# 
#  你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：satisfaction = [-1,-8,0,5,-9]
# 输出：14
# 解释：去掉第二道和最后一道菜，最大的 like-time 系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。 
# 
# 
#  示例 2： 
# 
#  
# 输入：satisfaction = [4,3,2]
# 输出：20
# 解释：可以按照任意顺序做菜 (2*1 + 3*2 + 4*3 = 20)
#  
# 
#  示例 3： 
# 
#  
# 输入：satisfaction = [-1,-4,-5]
# 输出：0
# 解释：大家都不喜欢这些菜，所以不做任何菜就可以获得最大的 like-time 系数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == satisfaction.length 
#  1 <= n <= 500 
#  -1000 <= satisfaction[i] <= 1000 
#  
# 
#  Related Topics 贪心 数组 动态规划 排序 👍 121 👎 0
