# 299 猜数字游戏
# https://leetcode.cn/problems/bulls-and-cows/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         cnt1, cnt2 = Counter(guess), Counter(secret)
#         b = 0
#         for x in "0123456789":
#             b += min(cnt1[x], cnt2[x])
#         a = 0
#         for x, y in zip(secret, guess):
#             a += x == y
#         return f"{a}A{b - a}B"

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt1, cnt2 = Counter(), Counter()
        a = 0
        for x, y in zip(secret, guess):
            if x == y:
                a += 1
            else:
                cnt1[x] += 1
                cnt2[y] += 1
            b = sum((cnt1 & cnt2).values())
        return f"{a}A{b}B"

# leetcode submit region end(Prohibit modification and deletion)
