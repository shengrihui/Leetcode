from typing import List


# 题目：100165. 找出数组中的美丽下标 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-i/
# 题库：https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-i

class Solution:
    def kmp(self, text: str, pattern: str) -> List[int]:
        m = len(pattern)
        pi = [0] * m
        c = 0
        for i in range(1, m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            pi[i] = c

        res = []
        c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = pi[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                res.append(i - m + 1)
                c = pi[c - 1]
        return res

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aa = self.kmp(s, a)
        bb = self.kmp(s, b)
        ans = []
        m = len(bb)
        j = 0
        for i in aa:
            while j < m and bb[j] < i - k:
                j += 1
            if j < m and abs(bb[j] - i) <= k:
                ans.append(i)
        return ans


s = Solution()
examples = [
    (dict(s="isawsquirrelnearmysquirrelhouseohmy", a="my", b="squirrel", k=15), [16, 33]),
    (dict(s="abcd", a="a", b="a", k=4), [0]),
]
for e, a in examples:
    print(a, e)
    print(s.beautifulIndices(**e))
