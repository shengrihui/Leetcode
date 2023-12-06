# 714 买卖股票的最佳时机含手续费
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy, sell = [0] * n, [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])  # max(之前买入今天不卖出（今天依然持有），之前卖出今天新买入)
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)  # max(今天不买，今天卖出手头持有的)
        return sell[-1]

# leetcode submit region end(Prohibit modification and deletion)


# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。 
# 
#  你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 
# 
#  返回获得利润的最大值。 
# 
#  注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出：8
# 解释：能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8 
# 
#  示例 2： 
# 
#  
# 输入：prices = [1,3,7,5,10,3], fee = 3
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 5 * 10⁴ 
#  1 <= prices[i] < 5 * 10⁴ 
#  0 <= fee < 5 * 10⁴ 
#  
# 
#  Related Topics 贪心 数组 动态规划 👍 1010 👎 0
