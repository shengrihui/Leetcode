# 70 爬楼梯
from functools import *


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# leetcode submit region begin(Prohibit modification and deletion)
# dp = [0] * 45
# dp[0] = 1
# dp[1] = 2
# for i in range(2, 45):
#     dp[i] = dp[i - 1] + dp[i - 2]


dp = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
      75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
      39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903]


class Solution:
    def climbStairs(self, n: int) -> int:
        return dp[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
