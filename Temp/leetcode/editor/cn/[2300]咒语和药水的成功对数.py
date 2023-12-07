# 2300 咒语和药水的成功对数
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m, l = len(spells), len(potions), max(potions) + 1
        suf = [0] * l  # suf[i] 在 potions 里大于等于 i 的有几个
        for x in potions:
            suf[x] += 1
        for i in range(1, l):
            suf[-i - 1] += suf[-i]
        ans = []
        suc = success - 1
        for x in spells:
            y = suc // x + 1
            ans.append(suf[y] if y < l else 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.successfulPairs(spells=
                        [7, 39, 34, 27, 1, 26, 16, 5, 29, 6, 30, 34],
                        potions=
                        [31, 3, 24, 26, 8, 34, 25, 39, 1, 32, 29, 1, 38, 28, 8, 38, 28, 9, 33, 15, 21, 36, 3, 37, 29,
                         23, 17, 16, 26, 18, 18, 12, 36, 30, 2, 38, 26, 11, 27, 36, 37, 1, 40, 38, 32, 12, 13, 27, 24,
                         28, 1, 31, 7, 15, 5, 32, 33, 18, 10, 11, 17, 11, 29, 18, 22, 23, 24, 6, 23, 38, 19, 15, 2, 24,
                         30, 10, 21],
                        success=
                        1564))
"""
spells =
[7,39,34,27,1,26,16,5,29,6,30,34]
potions =
[31,3,24,26,8,34,25,39,1,32,29,1,38,28,8,38,28,9,33,15,21,36,3,37,29,23,17,16,26,18,18,12,36,30,2,38,26,11,27,36,37,1,40,38,32,12,13,27,24,28,1,31,7,15,5,32,33,18,10,11,17,11,29,18,22,23,24,6,23,38,19,15,2,24,30,10,21]
success =
1564
"""
