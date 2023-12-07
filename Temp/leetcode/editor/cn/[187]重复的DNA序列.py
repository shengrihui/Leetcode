# 187 重复的DNA序列
from collections import *
from typing import *

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         s1 = set()
#         s2 = set()
#         for i in range(0, len(s) - 9):
#             t = s[i:i + 10]
#             if t in s1:
#                 s2.add(t)
#             s1.add(t)
#         return list(s2)

mp = {c: i for i, c in enumerate("ACGT")}


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        cnt = defaultdict(int)
        x = 0
        for c in s[:9]:
            x = (x << 2) | mp[c]
        for i, c in enumerate(s[9:], 9):
            x = ((x << 2) | mp[c]) & ((1 << 20) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i - 9:i + 1])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
