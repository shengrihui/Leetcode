# 1276 不浪费原料的汉堡制作方案
# https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # jumbo * 4 + small * 2 = tomatoSlices
        # jumbo + small = cheeseSlices
        jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
        small = (4 * cheeseSlices - tomatoSlices) / 2
        if jumbo == int(jumbo) and small == int(small) and jumbo >= 0 and small >= 0:
            return [int(jumbo), int(small)]
        return []
# leetcode submit region end(Prohibit modification and deletion)
