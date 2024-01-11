# 2085 统计出现过一次的公共字符串
# https://leetcode.cn/problems/count-common-words-with-one-occurrence/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1, cnt2 = Counter(words1), Counter(words2)
        # return sum(cnt1[w] == cnt2[w] == 1 for w in set(words1 + words2))
        return sum(v == cnt2[w] == 1 for w, v in cnt1.items())

# leetcode submit region end(Prohibit modification and deletion)
