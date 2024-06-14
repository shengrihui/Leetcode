# 2813 子序列最大优雅度
# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: -x[0])  # 按利润从大到小排序
        vis = set()  # 已经选的类别
        ans = total_profit = 0
        duplicate = []  # 重复出现的利润
        for i, (profit, cata) in enumerate(items):
            if i < k:  # 前k个先全选
                total_profit += profit
                if cata not in vis:
                    vis.add(cata)
                else:  # 已经选过的类别，将 profit 加入到 duplicate 中，栈中
                    duplicate.append(profit)
            # 之前没有出现过的类别，想着要从之前的选择中替换，
            # 类别数量会增加，total_profit 会减少，ans 可能会增加
            # 替换谁呢？
            # 选择之前出现过不止一次的那个类别的最少利润
            # 为什么要“不止一次”？因为如果是选只出现了一次的那个类别替换，类别数量一增一减没有变化，ans 一定变小
            # 这也是前面为什么要 cata 在 vis 里才入栈的原因
            elif cata not in vis and duplicate:
                vis.add(cata)
                total_profit += profit - duplicate.pop()
            ans = max(ans, total_profit + len(vis) ** 2)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
