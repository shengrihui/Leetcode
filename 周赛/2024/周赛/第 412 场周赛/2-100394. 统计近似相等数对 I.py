# 第 412 场周赛 第 2 题
# 题目：100394. 统计近似相等数对 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-412/problems/count-almost-equal-pairs-i/
# 题库：https://leetcode.cn/problems/count-almost-equal-pairs-i

from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def f(x, y):
            if x == y:
                return True
            diffx = []
            diffy = []
            while x or y:
                rx, ry = x % 10, y % 10
                if rx != ry:
                    diffx.append(rx)
                    diffy.append(ry)
                x //= 10
                y //= 10
            # print(x,y,diffx,diffy)
            if len(diffy) == 2 and diffx[0] == diffy[1] and diffx[1] == diffy[0]:
                return True
            return False

        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                ans += f(nums[i], nums[j])
        return ans


s = Solution()
examples = [
    (dict(nums=[3, 12, 30, 17, 21]), 2),
    (dict(nums=[1, 1, 1, 1, 1]), 10),
    (dict(nums=[123, 231]), 0),
]
for e, a in examples:
    print(a, e)
    print(s.countPairs(**e))
