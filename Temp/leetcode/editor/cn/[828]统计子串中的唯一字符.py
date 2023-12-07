# 828 统计子串中的唯一字符

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
