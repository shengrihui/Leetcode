# 题目：100187. 捕获黑皇后需要的最少移动次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-379/problems/minimum-moves-to-capture-the-queen/
# 题库：https://leetcode.cn/problems/minimum-moves-to-capture-the-queen

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:  # 车和皇后在同一行
            if a == c and (b < d < f or f < d < b):  # 象也在同一行且在车和皇后中间
                return 2
            return 1
        if b == f:  # 车和皇后在同一列，和上面差不多
            if b == d and (a < c < e or e < c < a):
                return 2
            return 1
        x = (c - e) / (d - f) if d != f else 0  # 象和皇后之间的斜率
        y = (c - a) / (d - b) if d != b else 0  # 象和车之间的斜率
        if x == 1 or x == -1:  # 象和皇后在斜线上
            if y == x and (c < a < e or e < a < c):  # 车夹在象和皇后中间
                return 2
            return 1
        return 2


s = Solution()
examples = [
    (dict(a=1, b=1, c=8, d=8, e=2, f=3), 2),
    (dict(a=5, b=3, c=3, d=4, e=5, f=2), 1),
    (dict(a=4, b=3, c=3, d=4, e=5, f=2), 2),
    (dict(a=8, b=4, c=7, d=5, e=5, f=5), 2),
    (dict(a=5, b=8, c=8, d=8, e=1, f=8), 1),
    (dict(a=1, b=1, c=1, d=4, e=1, f=8), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minMovesToCaptureTheQueen(**e))
