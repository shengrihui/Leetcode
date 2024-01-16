# 2744 最大字符串配对数目
# https://leetcode.cn/problems/find-maximum-number-of-string-pairs/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def maximumNumberOfStringPairs(self, words: List[str]) -> int:
#         ans = 0
#         n = len(words)
#         for i in range(n):
#             if words[i] == "":
#                 continue
#             for j in range(i + 1, n):
#                 if words[i] == words[j][::-1]:
#                     ans += 1
#                     words[j] = ""
#         return ans


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        se = set(words)
        for w in words:
            if w not in se:
                continue
            se.remove(w)
            rw = w[::-1]
            if rw in se:
                ans += 1
                se.remove(rw)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
