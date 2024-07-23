# 第 135 场双周赛 第 1 题
# 题目：100375. 求出硬币游戏的赢家
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-135/problems/find-the-winning-player-in-coin-game/
# 题库：https://leetcode.cn/problems/find-the-winning-player-in-coin-game

"""
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        i = 1
        while True:
            x -= 1
            y -= 4
            if x < 0 or y < 0:
                break
            i += 1
        return "Alice" if i % 2 == 0 else "Bob"
"""


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        return "Alice" if min(x, y // 4) % 2 else "Bob"


s = Solution()
examples = [
    (dict(x=2, y=7), "Alice"),
    (dict(x=4, y=11), "Bob"),
]
for e, a in examples:
    print(a, e)
    print(s.losingPlayer(**e))
