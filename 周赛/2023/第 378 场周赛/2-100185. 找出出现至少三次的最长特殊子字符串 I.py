from itertools import *


# 题目：100185. 找出出现至少三次的最长特殊子字符串 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-378/problems/find-longest-special-substring-that-occurs-thrice-i/
# 题库：https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-i

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        cnt = [[0] * (n + 2) for _ in range(26)]
        f = lambda c: ord(c) - 97
        i = 0
        while i < n:
            start = i
            ch = f(s[start])
            cnt[ch][2] -= 1
            cnt[ch][0] += 1
            i += 1
            while i < n and s[i] == s[i - 1]:
                cnt[ch][0] += 1
                cnt[ch][i - start + 2] -= 1
                i += 1
        ans = -1
        for ele in cnt:
            t = accumulate(ele, lambda x, y: x + y)
            for i, c in enumerate(t):
                if c >= 3 and i > ans:
                    ans = i
        return ans


s = Solution()
examples = [
    (dict(s="aaaa"), 2),
    (dict(s="abcdef"), -1),
    (dict(s="abcaba"), 1),
]
for e, a in examples:
    print(a, e)
    print(s.maximumLength(**e))
