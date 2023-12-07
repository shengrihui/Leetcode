# 318 最大单词长度乘积
from collections import *
from functools import *
from typing import *


# class Solution:
#     def maxProduct(self, words: List[str]) -> int:
#         ans = 0
#         n = len(words)
#         sets=[set(w) for w in words]
#         length=[len(w) for w in words]
#         for i in range(n):
#             for j in range(i + 1, n):
#                 s1 = sets[i]
#                 s2 = sets[j]
#                 if len(s1&s2)==0:
#                     t = length[i] * length[j]
#                     ans = t if t > ans else ans
#         return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)
        for w in words:
            mask = reduce(lambda x, y: x | (1 << (ord(y) - 97)), w, 0)
            l = len(w)  # 掩码相同只记录长度最长的
            masks[mask] = l if l > masks[mask] else masks[mask]
        ans = 0
        keys = list(masks.keys())
        m = len(keys)
        ans = 0
        for i in range(m):
            for j in range(i + 1, m):
                ki, kj = keys[i], keys[j]
                if ki & kj == 0:
                    ans = max(ans, masks[ki] * masks[kj])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
