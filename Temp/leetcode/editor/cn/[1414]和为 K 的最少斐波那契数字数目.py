# 1414 和为 K 的最少斐波那契数字数目
# https://leetcode.cn/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
fibo = [1, 1]
while fibo[-1] <= 1_000_000_000:
    fibo.append(fibo[-1] + fibo[-2])

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        i = bisect_left(fibo, k)
        s, ans = 0, 0
        while s < k:
            if s + fibo[i] <= k:
                s += fibo[i]
                ans += 1
            i -= 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
