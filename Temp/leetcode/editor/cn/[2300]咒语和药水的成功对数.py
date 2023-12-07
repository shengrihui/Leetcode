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

# 给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，potions[
# j] 表示第 j 瓶药水的能量强度。 
# 
#  同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。 
# 
#  请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# 输出：[4,0,3]
# 解释：
# - 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
# - 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
# - 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
# 所以返回 [4,0,3] 。
#  
# 
#  示例 2： 
# 
#  输入：spells = [3,1,2], potions = [8,5,8], success = 16
# 输出：[2,0,2]
# 解释：
# - 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
# - 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
# - 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
# 所以返回 [2,0,2] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == spells.length 
#  m == potions.length 
#  1 <= n, m <= 10⁵ 
#  1 <= spells[i], potions[i] <= 10⁵ 
#  1 <= success <= 10¹⁰ 
#  
# 
#  Related Topics 数组 双指针 二分查找 排序 👍 35 👎 0
