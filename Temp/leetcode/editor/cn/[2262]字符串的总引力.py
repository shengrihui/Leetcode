# 2262 字符串的总引力

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
