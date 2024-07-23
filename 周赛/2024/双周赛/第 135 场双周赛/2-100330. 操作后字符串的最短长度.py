# 第 135 场双周赛 第 2 题
# 题目：100330. 操作后字符串的最短长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-135/problems/minimum-length-of-string-after-operations/
# 题库：https://leetcode.cn/problems/minimum-length-of-string-after-operations

from collections import *


# class Solution:
#     def minimumLength(self, s: str) -> int:
#         @cache
#         def f(x: int) -> int:
#             if x <= 2:
#                 return x
#             return f(x - 2)
#
#         cnt = Counter(s)
#         return sum(f(x) for x in cnt.values())

# 奇数个最后剩 1 个
# 偶数个最后剩 2 个
# c 次最后剩余 (c - 1) % 2 + 1
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum((c - 1) % 2 + 1 for c in Counter(s).values())


s = Solution()
examples = [
    (dict(s="abaacbcbb"), 5),
    (dict(s="aa"), 2),
]
for e, a in examples:
    print(a, e)
    print(s.minimumLength(**e))
