# 第 138 场双周赛 第 2 题
# 题目：100399. 哈希分割字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-138/problems/hash-divided-string/
# 题库：https://leetcode.cn/problems/hash-divided-string


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = []
        n = len(s)
        a = ord('a')
        for i in range(0, n, k):
            sub = s[i:i + k]
            su = sum(ord(c) - a for c in sub)
            ans.append(chr(su % 26 + a))
        return "".join(ans)


# 灵神
from string import ascii_lowercase


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = []
        for i in range(0, len(s), k):
            total = sum(ord(c) for c in s[i: i + k]) - ord('a') * k
            ans.append(ascii_lowercase[total % 26])
        return ''.join(ans)


s = Solution()
examples = [
    (dict(s="abcd", k=2), "bf"),
    (dict(s="mxz", k=3), "i"),
]
for e, a in examples:
    print(a, e)
    print(s.stringHash(**e))
