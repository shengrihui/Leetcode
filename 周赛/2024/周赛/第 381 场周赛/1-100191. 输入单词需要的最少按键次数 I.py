# 题目：100191. 输入单词需要的最少按键次数 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-381/problems/minimum-number-of-pushes-to-type-word-i/
# 题库：https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-i

class Solution:
    def minimumPushes(self, word: str) -> int:
        # n = len(word)
        # if n <= 8: return n
        # if n <= 16: return 8 + 2 * (n - 8)
        # if n <= 24: return 24 + 3 * (n - 16)
        # return 48 + 4 * (n - 24)
        k, r = divmod(len(word), 8)
        return 4 * k * (k + 1) + r * (k + 1)


s = Solution()
examples = [
    (dict(word="abcde"), 5),
    (dict(word="xycdefghij"), 12),
    (dict(word="amrvxnhsewkoipjyuclgtdbfq"), 52),
]
for e, a in examples:
    print(a, e)
    print(s.minimumPushes(**e))
