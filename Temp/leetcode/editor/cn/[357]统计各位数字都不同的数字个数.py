# 357 统计各位数字都不同的数字个数
# https://leetcode.cn/problems/count-numbers-with-unique-digits/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 面向测试结果做题
        # return [1,10,91,739,5275,32491,168571,712891,2345851][n]

        # @cache
        # def dfs(i: int, j: int, k: bool) -> int:
        #     # i：现在是第几位，j：现在有多少个数字可以选，k：前面是否空
        #     if i <= 1:
        #         if k:  # 前面是空的
        #             return 10 ** i
        #         else:  # 前面不是空的，那就还剩多少种就返回多少种
        #             return j
        #     ans = 0
        #     if k:
        #         # 前面是空的，当前位是首位，这一位有9种，然后 i-1 仍然有9种（当前位不能0）
        #         ans += 9 * dfs(i - 1, 9, False)
        #         # 这一位仍然是空
        #         ans += dfs(i - 1, 10, True)
        #     else:
        #         # 当前位有 j 种，i-1 位有 j-1 种
        #         ans += j * dfs(i - 1, j - 1, False)
        #     return ans
        # return dfs(n, 10, True)

        # @cache
        # def dfs(i: int, j: int, k: bool) -> int:  # i：现在是第几位，j：现在有多少个数字可以选，k：前面是否空
        #     if i <= 1:
        #         return j
        #     return 9 * dfs(i - 1, 9, False) + dfs(i - 1, 10, True) if k else j * dfs(i - 1, j - 1, False)
        #
        # return dfs(n, 10, True) if n else 1

        乘法原理
        if n <= 1:
            return 10 ** n
        ans = 10
        t = 9  # 从两位数开始的最高位可以选 9 种
        for i in range(2, n + 1):
            cur = 10 - i + 1  # 当前位可以选择
            t *= cur  # i 位数的情况
            ans += t  # ans +t 之前是 i—1 位的情况
        return ans

# leetcode submit region end(Prohibit modification and deletion)
