# 1155 掷骰子等于目标和的方法数
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        mx = max(target, k)
        dp = [0 for _ in range(mx + 1)]
        for i in range(k):
            dp[i + 1] = 1
        for i in range(1, n):
            for j in range(mx, -1, -1):
                dp[j] = sum(dp[max(0, j - k):j]) % MOD
        return dp[target]


# leetcode submit region begin(Prohibit modification and deletion)
"""
转移方程：
dp[j] = dp[j-1] + dp[j-2] + dp[j-3] + ... + dp[j-k](j>k)
定义（前缀和）
s[j] = dp[0] + dp[1] + dp[2] + ... + dp[j]
那么：
dp[j] = s[j-1] - s[j-k-1]
s[j-k-1]，所以j>=k+1
j<k+1的时候，就是dp[j] = s[j-1]
j是目标值，
"""


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        mx = max(target, k)
        dp = [0 for _ in range(mx + 1)]
        for i in range(k):
            dp[i + 1] = 1
        for i in range(1, n):
            # for j in range(1, mx + 1):
            mx_j = min((i + 1) * k, mx)
            for j in range(1, mx_j + 1):  # 当前有 i+1 个骰子，最多投掷 (i+1)*k
                dp[j] += dp[j - 1]
            for j in range(mx_j, 0, -1):  # 最小到k+1
                dp[j] = (dp[j - 1] - (dp[j - k - 1] if j >= k + 1 else 0)) % MOD
        return dp[target]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(222616187, s.numRollsToTarget(30, 30, 500))
"""
1
6
3
2
6
7
30
30
500
2
6
6
2
12
8
"""

# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。 
# 
#  给定三个整数 n , k 和 target ，返回可能的方式(从总共 kⁿ 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 target 。 
# 
#  答案可能很大，你需要对 10⁹ + 7 取模 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1, k = 6, target = 3
# 输出：1
# 解释：你扔一个有 6 个面的骰子。
# 得到 3 的和只有一种方法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2, k = 6, target = 7
# 输出：6
# 解释：你扔两个骰子，每个骰子有 6 个面。
# 得到 7 的和有 6 种方法：1+6 2+5 3+4 4+3 5+2 6+1。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 30, k = 30, target = 500
# 输出：222616187
# 解释：返回的结果必须是对 10⁹ + 7 取模。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n, k <= 30 
#  1 <= target <= 1000 
#  
# 
#  Related Topics 动态规划 👍 201 👎 0
