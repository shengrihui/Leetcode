# 2663 字典序最小的美丽字符串
# https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1
        s[i] += 1
        while i < n:  # 0 <= i < n
            if s[i] == k:  # 需要进位
                if i == 0:
                    return ""
                s[i] = a
                i -= 1  # 看看前面有没有回文
                s[i] += 1
            elif i > 0 and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:  # 有回文
                s[i] += 1
            else:
                i += 1
        return "".join(list(map(chr, s)))

# leetcode submit region end(Prohibit modification and deletion)
