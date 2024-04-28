# 392 判断子序列
# https://leetcode.cn/problems/is-subsequence/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        # s 是不是 t 的子序列
        j = 0
        # 法一
        n = len(t)
        for c in s:
            while j < n and c != t[j]:
                j += 1
            j += 1  # 匹配上了，j 往后移动一个
            if j > n:
                return False
        return True

        # 法二 慢
        """
        n = len(s)
        for c in t:
            if c == s[j]:
                j += 1
                if j == n:
                    return True
        return False
        """
# leetcode submit region end(Prohibit modification and deletion)
