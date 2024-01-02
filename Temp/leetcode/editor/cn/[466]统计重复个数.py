# 466 统计重复个数
# https://leetcode.cn/problems/count-the-repetitions/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/count-the-repetitions/solutions/2588359/you-shi-xue-lao-ti-jie-de-yi-ti-by-wei-j-ow8i
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        s2_len = len(s2)
        d = {}
        for i in range(s2_len):
            cnt, j = 0, i
            for c in s1:
                if c == s2[j]:
                    j += 1
                if j == s2_len:
                    cnt += 1
                    j = 0
            d[i] = (cnt, j)
        ans, j = 0, 0
        for _ in range(n1):
            cnt, j = d[j]
            ans += cnt
        return ans // n2
# leetcode submit region end(Prohibit modification and deletion)
