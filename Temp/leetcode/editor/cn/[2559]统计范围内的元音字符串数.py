# 2559 统计范围内的元音字符串数
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        pre = list(map(int, [w[0] in "aeiou" and w[-1] in "aeiou" for w in words]))
        for i in range(1, n):
            pre[i] += pre[i - 1]
        ans = []
        for l, r in queries:
            ans.append(pre[r] - (pre[l - 1] if l > 0 else 0))
            # ans.append(sum(pre[l:r + 1]))
        return ans
# leetcode submit region end(Prohibit modification and deletion)
