# 3096 得到更多分数的最少关卡数目
# https://leetcode.cn/problems/minimum-levels-to-gain-more-points/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        # nums = [1 if x == 1 else -1 for x in possible]
        # pre = list(accumulate(nums, initial=0))
        # for i in range(len(nums) - 1):
        #     a, b = pre[i + 1], pre[-1] - pre[i + 1]
        #     if a > b:
        #         return i + 1
        # return -1

        # 把 0 看做 -1 后计算数组元素和
        # 解释 / 来源：
        # s = 0
        # for x in possible:
        #     # if x == 1:
        #     #     s += 1
        #     # else:
        #     #     x -= 1
        #     s += x * -1
        s = sum(possible) * 2 - len(possible)
        pre = 0
        for i, x in enumerate(possible[:-1]):
            pre += 2 * x - 1
            if pre > s - pre:  # `前缀比后缀大
                return i + 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
