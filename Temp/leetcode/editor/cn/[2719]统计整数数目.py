# 2719 统计整数数目
# https://leetcode.cn/problems/count-of-integers/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def f(high: str) -> int:
            @cache
            def dfs(i: int, s: int, is_limit: bool) -> int:
                if s > max_sum:
                    return 0
                if i == n:
                    return s >= min_sum
                res = 0
                up = int(high[i]) if is_limit else 9
                for d in range(up + 1):
                    res += dfs(i + 1, s + d, is_limit and d == up)
                return res % 1_000_000_007

            n = len(high)
            return dfs(0, 0, True) % 1_000_000_007

        return (f(num2) - f(num1) + (min_sum <= sum(map(int, num1)) <= max_sum)) % 1_000_000_007

# leetcode submit region end(Prohibit modification and deletion)
