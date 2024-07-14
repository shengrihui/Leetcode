# 394 字符串解码
# https://leetcode.cn/problems/decode-string/

# leetcode submit region begin(Prohibit modification and deletion)
"""
# 每一次 ] 都要将对应的 [ 里的这一段 res 重复 [ 前的次数
# 每一次 [ 都将刚刚记录的次数和到上一次未闭合的 [ 的字符串记录下来
# 到上一次未闭合的 [ 的字符串 就是 res
# 也就是说，res 遇到 [ 和次数一起入栈，遇到 ] 就重复次数加到上一个 res （栈顶）后面
# 最终 res 即使答案
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        mult = 0
        res = ""
        for i, c in enumerate(s):
            if "0" <= c <= "9":
                mult = mult * 10 + int(c)
            elif c == "[":
                st.append([mult, res])
                mult, res = 0, ""
            elif c == "]":
                last_mult, last_res = st.pop()
                res *= last_mult
                res = last_res + res
            else:
                res += c
        return res
"""


# 递归
class Solution:
    def decodeString(self, s: str) -> (int, str):
        def f(i: int) -> str:
            res, mult = "", 0
            while i < len(s):
                c = s[i]
                if "0" <= c <= "9":
                    mult = mult * 10 + int(c)
                elif c == "[":
                    i, r = f(i + 1)
                    res += mult * r
                    mult = 0
                elif c == "]":
                    return i, res
                else:
                    res += c
                i += 1
            return i, res  # 必须要有，当最后一个 ] 返回之后再 i += 1 ，i = len(s0

        return f(0)[1]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
