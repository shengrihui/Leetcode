# 1160 拼写单词
# https://leetcode.cn/problems/find-words-that-can-be-formed-by-characters/
from imports import *

# leetcode submit region begin(Prohibit modification and deletion)
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def check(s):
            for i in s:
                if s.count(i) > chars.count(i):
                    return 0
            return len(s)

        ans = 0
        for i in words:
            ans += check(i)
        return ans
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = Counter(chars)
        for string in words:
            if Counter(string) <= cnt:
                ans += len(string)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
