# 第 407 场周赛 第 2 题
# 题目：100335. 字符串元音游戏
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-407/problems/vowels-game-in-a-string/
# 题库：https://leetcode.cn/problems/vowels-game-in-a-string


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # if sum(c in "aeiou" for c in s) == 0:
        #     return False
        # return True

        # for c in s:
        #     if c in "aeiou":
        #         return True
        # return False

        return any(c in "aeiou" for c in s)


s = Solution()
examples = [
    (dict(s="leetcoder"), True),
    (dict(s="eeqee"), True),
    (dict(s="bbcd"), False),
]
for e, a in examples:
    print(a, e)
    print(s.doesAliceWin(**e))
