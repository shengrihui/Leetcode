# 第 140 场双周赛 第 2 题
# 题目：100374. 高度互不相同的最大塔高和
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-140/problems/maximize-the-total-height-of-unique-towers/
# 题库：https://leetcode.cn/problems/maximize-the-total-height-of-unique-towers

from typing import List

"""
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        mx = maximumHeight[0]
        for h in maximumHeight:
            if mx <= 0:
                return -1
            if mx > h:
                ans += h
                mx = h - 1
            else:
                ans += mx
                mx -= 1
        return ans
"""


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        ans = 0
        mx = maximumHeight[0]
        for h in maximumHeight:
            if mx <= 0:
                return -1
            mx = min(mx, h)
            ans += mx
            mx -= 1
        return ans


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        for i in range(1, len(maximumHeight)):
            maximumHeight[i] = min(maximumHeight[i], maximumHeight[i] - 1)
            if maximumHeight[i] <= 0:
                return -1
        return sum(maximumHeight)

        s = Solution()
        examples = [
            (dict(maximumHeight=[1, 10, 5, 1]), -1),
            (dict(maximumHeight=[2, 3, 4, 3]), 10),
            (dict(maximumHeight=[15, 10]), 25),
            (dict(maximumHeight=[2, 2, 1]), -1),

        ]

        for e, a in examples:
            print(a, e)
        print(s.maximumTotalSum(**e))
