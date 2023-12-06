# 828 统计子串中的唯一字符
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq

# class Solution:
#     def uniqueLetterString(self, s: str) -> int:
#         n = len(s)
#         left = [-1] * n
#         d = {}
#         for i, c in enumerate(s):
#             left[i] = d.get(c, -1)
#             d[c] = i
#         right = [n] * n
#         d.clear()
#         for i in range(n - 1, -1, -1):
#             right[i] = d.get(s[i], n)
#             d[s[i]] = i
#         ans = 0
#         for i, (l, r) in enumerate(zip(left, right)):
#             ans += (i - l) * (r - i)
#         return ans

# leetcode submit region begin(Prohibit modification and deletion)
"""
s = BCADEAFGA
total 就是 countUniqueChars 
是遍历到 s[i] 的时候以 s[i] 结尾的不同子字符串中唯一字符的总数，
然后加到 ans 里
比如当前比例到 A
_____________________________________________
以 s[i]=A 结尾     
的不同子字符串         唯一字符数   与没加 A 的变化量
            A           1        1
           GA           2        1
          FGA           3        1
         AFGA           2       -1原来有 AFG 3个唯一字符，现在只有 FG 了
        EAFGA           3       -1原来有 EAFG 4个唯一字符，现在只有 EFG 了
       DEAFGA           4       -1
      ADEAFGA           4       0 和原来一样，都只有 DEFG 4个唯一字符
     CADEAFGA           5       0
    BCADEAFGA           6       0
          total = 唯一字符数 和和
                = 以 s[i-1] 结尾的唯一字符数的和 + 变化量
    变化量 = 1.如果 s[j] 到 s[i] 没有与 s[i] 相同，
                那这一部分 s[i] 对以 s[i] 结尾的字符串是正贡献，
                也就是让这个字符串的唯一字符多了一个 +1
            2.如果 s[j] 到 s[i] 有一个与 s[i] 相同，
                那这一部分 s[i] 对以 s[i] 结尾的字符串是负贡献，
                也就是让这个字符串的唯一字符少了一个 -1
            3.如果 s[j] 到 s[i] 有不止一个与 s[i] 相同，
                那这一部分 s[i] 对以 s[i] 结尾的字符串是没有贡献，
                也就是不影响这个字符串的唯一字符数量
所以，变化量 = (i-last0[s[i]]) - (last0[s[i]]-last1[s[i]])
     （last0/1：上一次/上上一次 出现s[i]的位置）           
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last0 = {}
        last1 = {}
        ans = total = 0
        for i, c in enumerate(s):
            total += i - 2 * last0.get(c, -1) + last1.get(c, -1)
            ans += total
            last1[c] = last0.get(c, -1)
            last0[c] = i
        return ans

# leetcode submit region end(Prohibit modification and deletion)


# 我们定义了一个函数 countUniqueChars(s) 来统计字符串 s 中的唯一字符，并返回唯一字符的个数。 
# 
#  例如：s = "LEETCODE" ，则其中 "L", "T","C","O","D" 都是唯一字符，因为它们只出现一次，所以 
# countUniqueChars(s) = 5 。 
# 
#  本题将会给你一个字符串 s ，我们需要返回 countUniqueChars(t) 的总和，其中 t 是 s 的子字符串。输入用例保证返回值为 32 位整
# 数。 
# 
#  注意，某些子字符串可能是重复的，但你统计时也必须算上这些重复的子字符串（也就是说，你必须统计 s 的所有子字符串中的唯一字符）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s = "ABC"
# 输出: 10
# 解释: 所有可能的子串为："A","B","C","AB","BC" 和 "ABC"。
#      其中，每一个子串都由独特字符构成。
#      所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
#  
# 
#  示例 2： 
# 
#  
# 输入: s = "ABA"
# 输出: 8
# 解释: 除了 countUniqueChars("ABA") = 1 之外，其余与示例 1 相同。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "LEETCODE"
# 输出：92
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 只包含大写英文字符 
#  
# 
#  Related Topics 哈希表 字符串 动态规划 👍 373 👎 0
