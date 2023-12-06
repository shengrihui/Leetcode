# 2262 字符串的总引力
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq

# leetcode submit region begin(Prohibit modification and deletion)
"""
s = "abbca"
从左往右遍历整个字符串
以当前这个字符为开头到当前遍历到的字符结尾的这个子串有多少个不同的字符     ans=和
a
1           ans1 = 1
a b       
2 1         ans2 = 3 = ans1 + 2
a b b
2 1 1       ans3 = 4 = ans2 + 1
a b b c
3 2 2 1     ans4 = 8 = ans3 + 4
a b b c a
3 3 3 2 1   ans5 = 12 = ans4 + 4
规律（总结）
ans[x] = ans[x-1] + 当前遍历到的这个字符上一次出现的位置（不包括）到现在这个位置（包括）的长度
"""


class Solution:
    def appealSum(self, s: str) -> int:
        ans = a = 0
        last = {}
        for i, c in enumerate(s):
            a += i - last.get(c, -1)
            ans += a
            last[c] = i
        return ans

# leetcode submit region end(Prohibit modification and deletion)


# 字符串的 引力 定义为：字符串中 不同 字符的数量。 
# 
#  
#  例如，"abbca" 的引力为 3 ，因为其中有 3 个不同字符 'a'、'b' 和 'c' 。 
#  
# 
#  给你一个字符串 s ，返回 其所有子字符串的总引力 。 
# 
#  子字符串 定义为：字符串中的一个连续字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abbca"
# 输出：28
# 解释："abbca" 的子字符串有：
# - 长度为 1 的子字符串："a"、"b"、"b"、"c"、"a" 的引力分别为 1、1、1、1、1，总和为 5 。
# - 长度为 2 的子字符串："ab"、"bb"、"bc"、"ca" 的引力分别为 2、1、2、2 ，总和为 7 。
# - 长度为 3 的子字符串："abb"、"bbc"、"bca" 的引力分别为 2、2、3 ，总和为 7 。
# - 长度为 4 的子字符串："abbc"、"bbca" 的引力分别为 3、3 ，总和为 6 。
# - 长度为 5 的子字符串："abbca" 的引力为 3 ，总和为 3 。
# 引力总和为 5 + 7 + 7 + 6 + 3 = 28 。
#  
# 
#  示例 2： 
# 
#  输入：s = "code"
# 输出：20
# 解释："code" 的子字符串有：
# - 长度为 1 的子字符串："c"、"o"、"d"、"e" 的引力分别为 1、1、1、1 ，总和为 4 。
# - 长度为 2 的子字符串："co"、"od"、"de" 的引力分别为 2、2、2 ，总和为 6 。
# - 长度为 3 的子字符串："cod"、"ode" 的引力分别为 3、3 ，总和为 6 。
# - 长度为 4 的子字符串："code" 的引力为 4 ，总和为 4 。
# 引力总和为 4 + 6 + 6 + 4 = 20 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 哈希表 字符串 动态规划 👍 74 👎 0
