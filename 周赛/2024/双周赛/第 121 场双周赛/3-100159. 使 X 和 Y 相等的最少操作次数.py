from functools import cache

# 题目：100159. 使 X 和 Y 相等的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-121/problems/minimum-number-of-operations-to-make-x-and-y-equal/
# 题库：https://leetcode.cn/problems/minimum-number-of-operations-to-make-x-and-y-equal

# BFS
"""
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        q = deque()
        q.append(x)
        step = 0
        vis = {x}
        while q:
            for _ in range(len(q)):
                xx = q.popleft()
                # print(xx)
                for i in [11, 5]:
                    if xx % i == 0 and (nx := xx // i) not in vis:
                        if nx == y:
                            return step + 1
                        q.append(nx)
                        vis.add(nx)
                for i in [1, -1]:
                    if (nx := xx + i) not in vis and nx > 0:
                        if nx == y:
                            return step + 1
                        q.append(nx)
                        vis.add(nx)

            step += 1
"""


# 记忆化搜索
# 时间复杂度： O((logx)^2)
class Solution:
    @cache
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x
        return min(x - y,  # 全部采用 -1 操作
                   # 将 x 向下变成 11 的倍数，x%11 x多少次变成11的倍数，+1 //11这一次的操作
                   self.minimumOperationsToMakeEqual(x // 11, y) + x % 11 + 1,
                   # 将 x 向上变成 11 的倍数
                   self.minimumOperationsToMakeEqual(x // 11 + 1, y) + 11 - x % 11 + 1,
                   self.minimumOperationsToMakeEqual(x // 5, y) + x % 5 + 1,
                   self.minimumOperationsToMakeEqual(x // 5 + 1, y) + +5 - x % 5 + 1,
                   )


s = Solution()
examples = [
    (dict(x=26, y=1), 3),
    (dict(x=54, y=2), 4),
    (dict(x=25, y=30), 5),
    (dict(x=10 ** 18, y=30), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperationsToMakeEqual(**e))
