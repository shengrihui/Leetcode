# 14 最长公共前缀
# https://leetcode.cn/problems/longest-common-prefix/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for col in zip(*strs):
            if len(set(col)) > 1:
                break
            i += 1
        return strs[0][:i]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for j, c in enumerate(s0):
            for s in strs:
                if len(s) == j or s[j] != c:
                    return s[:j]
        return s0
# leetcode submit region end(Prohibit modification and deletion)
