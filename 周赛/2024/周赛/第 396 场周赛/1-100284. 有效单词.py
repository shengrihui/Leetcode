# 第 396 场周赛 第 1 题
# 题目：100284. 有效单词
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-396/problems/valid-word/
# 题库：https://leetcode.cn/problems/valid-word

from collections import *


class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3 or '@' in word or '#' in word or '$' in word:
            return False
        cnt = Counter(word)
        for c in "aeiouAEIOU":
            if cnt[c] > 0:
                break
        else:
            return False
        for c in "qwrtypsdfghjklzxcvnbm":
            if cnt[c] > 0 or cnt[c.upper()] > 0:
                break
        else:
            return False
        return True


"""
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = conso = False
        for c in word:
            if c in "@#$":
                return False
            if c.isalpha():
                if c.lower() in "aeiou":
                    vowel = True
                else:
                    conso = True
        return vowel and conso
"""

s = Solution()
examples = [
    (dict(word="234Adas"), True),
    (dict(word="b3"), False),
    (dict(word="a3$e"), False),
]
for e, a in examples:
    print(a, e)
    print(s.isValid(**e))
