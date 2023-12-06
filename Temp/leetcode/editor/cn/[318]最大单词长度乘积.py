# 318 最大单词长度乘积
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


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


# 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母
# 。如果不存在这样的两个单词，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出：16 
# 解释：这两个单词为 "abcw", "xtfn"。 
# 
#  示例 2： 
# 
#  
# 输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
# 输出：4 
# 解释：这两个单词为 "ab", "cd"。 
# 
#  示例 3： 
# 
#  
# 输入：words = ["a","aa","aaa","aaaa"]
# 输出：0 
# 解释：不存在这样的两个单词。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words[i] 仅包含小写字母 
#  
# 
#  Related Topics 位运算 数组 字符串 👍 436 👎 0
