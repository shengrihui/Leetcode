# 2376 统计特殊整数
# https://leetcode.cn/problems/count-special-integers/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 现在填第 i 位，
        # i 前面的数的集合是 mask
        # is_limit true 这一位填 [0,s[i]] ，false 填 [0,9]
        # is_num 前面填数字了没，false 没有填数字，不能填 0 但也可以不填
        @cache
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return is_num
            res = 0
            if not is_num:
                res += dfs(i + 1, mask, False, is_num)  # 这一位不填
            up = int(s[i]) if is_limit else 9
            low = 1 if not is_num else 0  # not is_num == 前面没有填过数字 == 这是最高位 == 从 1 开始枚举
            for d in range(low, up + 1):  # 枚举这一位可以填的数字
                if not mask >> d & 1:
                    res += dfs(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res

        s = str(n)
        return dfs(0, 0, True, False)
# leetcode submit region end(Prohibit modification and deletion)
