# 638 大礼包
# https://leetcode.cn/problems/shopping-offers/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @cache
        def dfs(cur_needs):
            res = sum(p * ne for p, ne in zip(price, cur_needs))  # 不用大礼包
            for sp in special:
                sp_price = sp[-1]
                nxt_need = []
                for need, s in zip(cur_needs, sp):
                    if need < s:
                        break
                    nxt_need.append(need - s)
                else:
                    res = min(res, dfs(tuple(nxt_need)) + sp_price)
            return res

        # new_special = []
        # for sp in special:
        #     # 大礼包非空，且比单买是要优惠的
        #     if sum(sp[:-1]) > 0 and sum(p * s for p, s in zip(price, sp)) > sp[-1]:
        #         new_special.append(sp)
        # special = new_special
        return dfs(tuple(needs))

# leetcode submit region end(Prohibit modification and deletion)
