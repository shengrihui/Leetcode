# 2390 从字符串中移除星号
# https://leetcode.cn/problems/removing-stars-from-a-string/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for c in s:
            if c == "*":
                st.pop()
            else:
                st.append(c)
        return "".join(st)
# leetcode submit region end(Prohibit modification and deletion)
