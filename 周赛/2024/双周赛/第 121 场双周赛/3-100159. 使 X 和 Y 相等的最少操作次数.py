from collections import *


# 题目：100159. 使 X 和 Y 相等的最少操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-121/problems/minimum-number-of-operations-to-make-x-and-y-equal/
# 题库：https://leetcode.cn/problems/minimum-number-of-operations-to-make-x-and-y-equal

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


s = Solution()
examples = [
    (dict(x=26, y=1), 3),
    (dict(x=54, y=2), 4),
    (dict(x=25, y=30), 5),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperationsToMakeEqual(**e))
