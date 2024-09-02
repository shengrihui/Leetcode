# 2586 统计范围内的元音字符串数
# https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        return sum(word[0] in "aeiou" and word[-1] in "aeiou" for word in words[left:right + 1])
# leetcode submit region end(Prohibit modification and deletion)
