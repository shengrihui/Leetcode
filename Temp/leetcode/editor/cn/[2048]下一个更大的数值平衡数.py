# 2048 下一个更大的数值平衡数
# https://leetcode.cn/problems/next-greater-numerically-balanced-number/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(x: int) -> bool:
            cnt = defaultdict(int)
            while x:
                r = x % 10
                if 1 <= r <= 6:
                    cnt[r] += 1
                    x //= 10
                else:
                    return False
            return all(i == v for i, v in cnt.items())
        i = n + 1
        while True:
            if check(i):
                return i
            i += 1
# leetcode submit region end(Prohibit modification and deletion)
