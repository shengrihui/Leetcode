# 1954 收集足够苹果的最小花园周长
# https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def check(x: int) -> bool:
            y0 = x * (x + 1) // 2
            yall = (x + 1) * (y0 + y0 + x * x) // 2
            return 4 * yall >= neededApples

        l, r = 0, 10 ** 5
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l * 8
# leetcode submit region end(Prohibit modification and deletion)
