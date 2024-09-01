# 第 413 场周赛 第 1 题
# 题目：100410. 检查棋盘方格颜色是否相同
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-413/problems/check-if-two-chessboard-squares-have-the-same-color/
# 题库：https://leetcode.cn/problems/check-if-two-chessboard-squares-have-the-same-color


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # x, y = ord(coordinate1[0]) - ord('a') + 1, int(coordinate1[1])
        # xx, yy = ord(coordinate2[0]) - ord('a') + 1, int(coordinate2[1])
        # d, dd = y - x, yy - xx
        # return abs(d - dd) % 2 == 0

        # 字母和数字对应的 ASCII 都是奇数或者偶数，那格子就是黑色
        # 奇偶相同黑色，不同是白色
        # 两个 ASCII 加起来是偶数，黑色
        return (ord(coordinate1[0]) + ord(coordinate1[1])) % 2 == (ord(coordinate2[0]) + ord(coordinate2[1])) % 2


s = Solution()
examples = [
    (dict(coordinate1="a1", coordinate2="c3"), True),
    (dict(coordinate1="a1", coordinate2="h3"), False),
]
for e, a in examples:
    print(a, e)
    print(s.checkTwoChessboards(**e))
