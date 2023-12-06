from typing import List
from collections import *
from itertools import *


# 题目：# 8048. 最大二进制奇数
# 题目链接：
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = s.count("1")
        zero = s.count("0")
        return "1" * (one - 1) + "0" * zero + "1"


s = Solution()
examples = [
    # (dict(),),
    # (dict(),),
]
for e, a in examples:
    print(a, e)
print(s.findAnagrams(**e))
