# 第 405 场周赛 第 1 题
# 题目：100339. 找出加密后的字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-405/problems/find-the-encrypted-string/
# 题库：https://leetcode.cn/problems/find-the-encrypted-string


# class Solution:
#     def getEncryptedString(self, s: str, k: int) -> str:
#         ans = []
#         for i, c in enumerate(list(s)):
#             ans.append(s[(i + k) % len(s)])
#         return "".join(ans)


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k %= len(s)
        return s[k:] + s[:k]


s = Solution()
examples = [
    (dict(s="dyt", k=4), "ytd"),
    (dict(s="dart", k=3), "tdar"),
    (dict(s="aaa", k=1), "aaa"),
]
for e, a in examples:
    print(a, e)
    print(s.getEncryptedString(**e))
