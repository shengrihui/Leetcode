# 902 最大为 N 的数字组合
# https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        @cache
        def dfs(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return is_num
            res = 0
            if not is_num:
                res += dfs(i + 1, False, is_num)  # 这一位不填
            up = s[i] if is_limit else '9'
            for d in digits:  # 枚举这一位可以填的数字
                if d > up:
                    break
                res += dfs(i + 1, is_limit and d == up, True)
            return res

        s = str(n)
        return dfs(0, True, False)
# leetcode submit region end(Prohibit modification and deletion)
