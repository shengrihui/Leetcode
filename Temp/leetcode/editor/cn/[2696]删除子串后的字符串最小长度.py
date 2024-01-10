# 2696 删除子串后的字符串最小长度
# https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minLength(self, s: str) -> int:
        st = ["#"]
        for c in s:
            if c == "B" and st[-1] == "A" or c == "D" and st[-1] == "C":
                st.pop()
            else:
                st.append(c)
        return len(st) - 1
# leetcode submit region end(Prohibit modification and deletion)
