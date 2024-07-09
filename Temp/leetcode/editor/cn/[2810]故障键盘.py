# 2810 故障键盘
# https://leetcode.cn/problems/faulty-keyboard/


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def finalString(self, s: str) -> str:
        q = deque()
        tail = True
        for c in s:
            if c == "i":
                tail = not tail
            elif tail:
                q.append(c)
            else:
                q.appendleft(c)
        return "".join(q if tail else reversed(q))

# class Solution:
#     def finalString(self, s: str) -> str:
#         ans = ""
#         for c in s:
#             if c == "i":
#                 ans = ans[::-1]
#             else:
#                 ans += c
#         return ans
# leetcode submit region end(Prohibit modification and deletion)
