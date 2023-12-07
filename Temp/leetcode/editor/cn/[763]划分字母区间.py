# 763 划分字母区间
from typing import *


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        i = 0
        left, right = 0, 0
        n = len(s)
        while i < n:
            j = s.rfind(s[i])
            if j > right:
                right = j
            if i == right:
                ans.append(right - left + 1)
                left = right + 1
            i += 1
        return ans


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
        ans = []
        i = 0
        left, right = 0, 0
        n = len(s)
        while i < n:
            right = max(right, last[ord(s[i]) - 97])
            if i == right:
                ans.append(right - left + 1)
                left = right + 1
            i += 1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
