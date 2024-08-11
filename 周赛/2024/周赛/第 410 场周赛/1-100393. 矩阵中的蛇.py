# 第 410 场周赛 第 1 题
# 题目：100393. 矩阵中的蛇
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-410/problems/snake-in-matrix/
# 题库：https://leetcode.cn/problems/snake-in-matrix

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        d = {"UP": -n, "DOWN": n, "LEFT": -1, "RIGHT": 1}
        return sum(d[c] for c in commands)


s = Solution()
examples = [
    (dict(n=2, commands=["RIGHT", "DOWN"]), 3),
    (dict(n=3, commands=["DOWN", "RIGHT", "UP"]), 1),
]
for e, a in examples:
    print(a, e)
    print(s.finalPositionOfSnake(**e))
