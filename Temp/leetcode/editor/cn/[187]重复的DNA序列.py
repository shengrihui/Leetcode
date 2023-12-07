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


# DNA序列 由一系列核苷酸组成，缩写为
#  'A', 'C', 'G' 和
#  'T'.。 
# 
#  
#  例如，
#  "ACGAATTCCG" 是一个 DNA序列 。 
#  
# 
#  在研究 DNA 时，识别 DNA 中的重复序列非常有用。 
# 
#  给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 10⁵ 
#  s[i]=='A'、'C'、'G' or 'T' 
#  
# 
#  Related Topics 位运算 哈希表 字符串 滑动窗口 哈希函数 滚动哈希 👍 509 👎 0
