# 2828 判别首字母缩略词
# https://leetcode.cn/problems/check-if-a-string-is-an-acronym-of-words/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for c, w in zip(s, words):
            if c != w[0]:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
