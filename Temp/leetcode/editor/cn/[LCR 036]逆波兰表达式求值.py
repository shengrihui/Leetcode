# LCR 036 逆波兰表达式求值
# https://leetcode.cn/problems/8Zf90G/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for s in tokens:
            if s not in "+-*/":
                st.append(int(s))
                continue
            a = st.pop()
            b = st.pop()
            match s:
                case "+":
                    st.append(a + b)
                case "-":
                    st.append(b - a)
                case "*":
                    st.append(a * b)
                case "/":
                    st.append(int(b / a))
        return st[-1]
    # leetcode submit region end(Prohibit modification and deletion)
