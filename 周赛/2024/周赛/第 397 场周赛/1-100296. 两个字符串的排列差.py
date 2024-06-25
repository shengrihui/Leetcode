# 第 397 场周赛 第 1 题
# 题目：100296. 两个字符串的排列差
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-397/problems/permutation-difference-between-two-strings/
# 题库：https://leetcode.cn/problems/permutation-difference-between-two-strings

"""
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ss = {}
        tt = {}
        for i, (x, y) in enumerate(zip(s, t)):
            ss[x] = i
            tt[y] = i
        ans = 0
        for x in s:
            ans += abs(ss[x] - tt[x])
        return ans
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {c: i for i, c in enumerate(s)}
        ans = 0
        for i, c in enumerate(t):
            ans += abs(i - pos[c])
        return ans


s = Solution()
examples = [
    (dict(s="abc", t="bac"), 2),
    (dict(s="abcde", t="edbac"), 12),
]
for e, a in examples:
    print(a, e)
    print(s.findPermutationDifference(**e))
