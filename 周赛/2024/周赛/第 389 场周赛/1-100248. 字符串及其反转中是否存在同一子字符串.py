# 第 389 场周赛 第 1 题
# 题目：100248. 字符串及其反转中是否存在同一子字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-389/problems/existence-of-a-substring-in-a-string-and-its-reverse/
# 题库：https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse

from itertools import *


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        st = set()
        for x, y in pairwise(s):
            st.add((x, y))
            if (y, x) in st:
                return True
        return False


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 1):
            sub = s[i:i + 2]
            if sub in s[::-1]:
                return True
        return False
