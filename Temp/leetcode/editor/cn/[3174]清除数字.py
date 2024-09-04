# 3174 清除数字
# https://leetcode.cn/problems/clear-digits/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isdigit():
                st.pop()
            else:
                st.append(c)
        return "".join(st)
# leetcode submit region end(Prohibit modification and deletion)
