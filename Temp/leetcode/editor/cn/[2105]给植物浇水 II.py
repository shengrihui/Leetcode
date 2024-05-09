# 2105 给植物浇水 II
# https://leetcode.cn/problems/watering-plants-ii/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i, j = 0, len(plants) - 1
        ans = 0
        c1, c2 = capacityA, capacityB
        while i < j:
            if c1 < plants[i]:
                ans += 1
                c1 = capacityA
            if c2 < plants[j]:
                ans += 1
                c2 = capacityB
            c1 -= plants[i]
            c2 -= plants[j]
            i += 1
            j -= 1
        if i == j:
            if max(c1, c2) < plants[i]:
                ans += 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
