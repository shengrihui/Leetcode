# 2412 完成所有交易的初始最少钱数
# https://leetcode.cn/problems/minimum-money-required-before-transactions/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
要求任意一种顺序都能完成交易，就要要考虑最坏的情况下也能完成交易。
最坏的情况就是先亏钱，后赚钱。
为什么不是先赚钱后亏钱呢？因为如果先赚钱后亏钱得到的初始前数，不一定能满足先亏钱的顺序。

最坏的情况也就是，就是要满足在最穷的时候也能完成交易。
最穷的时候就是亏完所有前的时候。

记初始前是initMoney，一共亏的钱是total_lose。
1. 在亏完后要开始赚，满足 initMoney - total_lose >= cost 
    为了满足所有顺序，cost 应当是赚钱（包括不赚不亏）的最大值
2. 要完成所有亏钱的交易，initMoney 亏完 total_lose 之外还必须要保证最后一笔亏钱的能交易成功
    在最后一笔亏钱交易之前，还有 initMoney - total_lose + (cost - cashBack) 
    也就是 initMoney - total_lose + (cost - cashBack)e >= cost
    化简 initMoney >= total_loss + cashBack

两种情况  total_lose 加的分别是赚钱和亏钱时 cost,cashBack 的较小值
"""


# https://leetcode.cn/problems/minimum-money-required-before-transactions/solutions/1830862/by-endlesscheng-lvym
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_lose = mx = 0
        for x, y in transactions:
            total_lose += x - y if x > y else 0
            mx = max(mx, min(x, y))
        return total_lose + mx
# leetcode submit region end(Prohibit modification and deletion)
