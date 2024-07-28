# 第 408 场周赛 第 1 题
# 题目：100377. 判断是否可以赢得数字游戏
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-408/problems/find-if-digit-game-can-be-won/
# 题库：https://leetcode.cn/problems/find-if-digit-game-can-be-won

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        # a = b = 0
        # for x in nums:
        #     if x < 10:
        #         a += x
        #     else:
        #         b += x
        # return a != b
        s = 0
        for x in nums:
            s += x if x < 10 else -x
        return s != 0
        # return sum(x if x < 10 else -x for x in nums) != 0


s = Solution()
examples = [
    (dict(nums=[1, 2, 3, 4, 10]), False),
    (dict(nums=[1, 2, 3, 4, 5, 14]), True),
    (dict(nums=[5, 5, 5, 25]), True),
]
for e, a in examples:
    print(a, e)
    print(s.canAliceWin(**e))
