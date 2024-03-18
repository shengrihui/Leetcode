# 第 384 场周赛 第 3 题
# 题目：100219. 回文字符串的最大数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-384/problems/maximum-palindromes-after-operations/
# 题库：https://leetcode.cn/problems/maximum-palindromes-after-operations

from collections import *
from typing import List


# class Solution:
#     def maxPalindromesAfterOperations(self, words: List[str]) -> int:
#         cnt = sorted(Counter("".join(words)).values(), reverse=True)
#         lens = sorted([len(w) for w in words])
#         ans = 0
#         i, j = 0, 0
#         # print(cnt, lens)
#         while i < len(lens) and j < len(cnt):
#             l = lens[i]
#             if cnt[j] == 1 and l > 1: break
#             if cnt[j] >= l:
#                 ans += 1
#                 cnt[j] -= l
#                 i += 1
#             else:
#                 lens[i] -= cnt[j]
#                 j += 1
#         return ans

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        cnt = Counter("".join(words))
        cnts = sum(c // 2 for c in cnt.values())
        lens = sorted([len(w) // 2 for w in words])
        ans = 0
        for i, l in enumerate(lens):
            if cnts < l:  # 没法构成回文串了
                break
            cnts -= l
            ans += 1
        return ans


s = Solution()
examples = [
    (dict(words=["bwma", "a"]), 1),
    (dict(words=["cbc", "a"]), 2),
    (dict(words=["abc", "ab"]), 2),
    (dict(words=["abbb", "ba", "aa"]), 3),
    (dict(words=["cd", "ef", "a"]), 1),
    (dict(words=["a", "b"]), 2),
]
for e, a in examples:
    print(a, e)
    print(s.maxPalindromesAfterOperations(**e))
