# 第 417 场周赛 第 1 题
# 题目：100446. 找出第 K 个字符 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-417/problems/find-the-k-th-character-in-string-game-i/
# 题库：https://leetcode.cn/problems/find-the-k-th-character-in-string-game-i

ss = "a"
while len(ss) <= 500:
    t = []
    for c in ss:
        t.append(chr(ord("a") + (ord(c) + 1 - ord("a")) % 26))
    ss += "".join(t)


# print(ss)

class Solution:
    def kthCharacter(self, k: int) -> str:
        return ss[k - 1]


s = Solution()
examples = [
    (dict(k=5), "b"),
    (dict(k=10), "c"),
]
for e, a in examples:
    print(a, e)
    print(s.kthCharacter(**e))
