# 2734 执行子串操作后的字典序最小字符串
# https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        for i, c in enumerate(s):
            if c == "a":
                continue
            for j in range(i, len(s)):
                if s[j] == "a":
                    break
                s[j] = chr(ord(s[j]) - 1)
            return "".join(s)
        s[-1] = "z"  # 全是 a
        return "".join(s)
# leetcode submit region end(Prohibit modification and deletion)
