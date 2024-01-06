# 383 赎金信
# https://leetcode.cn/problems/ransom-note/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1, cnt2 = Counter(ransomNote), Counter(magazine)
        return all(v <= cnt2[k] for k, v in cnt1.items())
# leetcode submit region end(Prohibit modification and deletion)
