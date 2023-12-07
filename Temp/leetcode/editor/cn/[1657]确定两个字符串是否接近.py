# 1657 确定两个字符串是否接近
from collections import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt.keys()) == sorted(cnt2.keys()) and sorted(cnt.values()) == sorted(cnt2.values())
# leetcode submit region end(Prohibit modification and deletion)
