from typing import List


# 题目：# 7005. 判断通过操作能否让字符串相等 II
# 题目链接：https://leetcode.cn/contest/biweekly-contest-112/problems/check-if-strings-can-be-made-equal-with-operations-ii/
# class Solution:
#     def checkStrings(self, s1: str, s2: str) -> bool:
#         from collections import deque
#         s_set = set()
#         s_set2 = set()
#         q1 = deque()
#         q2 = deque()
#         q1.append(s1)
#         q2.append(s2)
#         s_set.add(s1)
#         s_set2.add(s2)
#         n = len(s1)
#         while q1 and q2:
#             if len(q1) < len(q2):
#                 q = q1
#                 now_set = s_set
#                 another_s = s_set2
#             else:
#                 q = q2
#                 now_set = s_set2
#                 another_s = s_set
#             s = q.popleft()
#             for i in range(n - 2):
#                 # print(i, n)
#                 new_s = "".join([s[:i], s[i + 2], s[i + 1], s[i], s[i + 3:]])
#                 # print(new_s)
#                 if new_s in another_s:
#                     return True
#                 if new_s not in now_set:
#                     q.append(new_s)
#                     now_set.add(new_s)
#         return False

# class Solution:
#     def checkStrings(self, s1: str, s2: str) -> bool:
#         ji_1 = sorted(list(s1[::2]))
#         ou_1 = sorted(list(s1[1::2]))
#         ji_2 = sorted(list(s2[::2]))
#         ou_2 = sorted(list(s2[1::2]))
#         # print(ji_1 == ji_2, ji_1, ji_2)
#         # print(ou_2 == ou_1, ou_2, ou_1)
#         if ji_1 == ji_2 and ou_1 == ou_2:
#             return True
#         return False


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return sorted(list(s1[::2])) == sorted(list(s2[::2])) and sorted(list(s1[1::2])) == sorted(list(s2[1::2]))


s = Solution()
examples = [
    (dict(s1="abcdba", s2="cabdab"), True),
    (dict(s1="abe", s2="bea"), False),
    (dict(s1="aavizsxpqhxztrwi", s2="zvisqatzpaxhixwr"), False),
    (dict(s1="yviqgzqwetjqwnmmbupitdsjdvophjhkiivtbsgehlxzestjjrqwahxcaafafgdxjiocwgnqbmoxbcbpiwz",
          s2="yjowhiiitgdesjzjwvqqnuonirjggtbpjmpwmzapjsbcqahxfidqoxotbavmfzbcblxvesxwgcahhqwkedi"), False),
]
for e, a in examples:
    print(a, e)
    print(s.checkStrings(**e))
