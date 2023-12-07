# 20 有效的括号


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {"(": ")", ")": "(",
             "[": "]", "]": "[",
             "{": "}", "}": "{"}
        for c in s:
            if c in "{[(":
                st.append(c)
            if c in "}])":
                if st == [] or st[-1] != d[c]:
                    return False
                else:
                    st.pop()
        return st == []
# leetcode submit region end(Prohibit modification and deletion)
