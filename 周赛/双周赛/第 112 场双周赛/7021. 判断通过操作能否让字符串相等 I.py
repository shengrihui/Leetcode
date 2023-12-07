# 题目：# 7021. 判断通过操作能否让字符串相等 I
# 题目链接：
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a, b, c, d = s1.split()
        if a + b + c + d == s2 or \
                a + d + c + b == s2 or \
                c + b + a + d == s2 or \
                c + d + a + b == s2:
            return True
        return False
