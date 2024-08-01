# LCP 40 心算挑战
# https://leetcode.cn/problems/uOAnQW/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        # 前 cnt 和就是偶数就直接返回
        # 否钻，
        # 减去前 cnt 的最小奇数加剩余最大偶数
        # 减去前 cnt 的最小偶数加剩余最大奇数
        mn_odd_1, mn_even_1 = inf, inf
        for x in cards[:cnt]:
            if x % 2 == 1 and x < mn_odd_1:
                mn_odd_1 = x
            elif x % 2 == 0 and x < mn_even_1:
                mn_even_1 = x
        mx_odd_2, mx_even_2 = -inf, -inf
        for x in cards[cnt:]:
            if x % 2 == 1 and x > mx_odd_2:
                mx_odd_2 = x
            elif x % 2 == 0 and x > mx_even_2:
                mx_even_2 = x

        s = sum(cards[:cnt])
        if s % 2 == 0:
            return s
        ans = 0
        if mn_odd_1 != inf and mx_even_2 != -inf:
            ans = max(ans, s - mn_odd_1 + mx_even_2)
        if mn_even_1 != inf and mx_odd_2 != -inf:
            ans = max(ans, s - mn_even_1 + mx_odd_2)

        return ans

# leetcode submit region end(Prohibit modification and deletion)
