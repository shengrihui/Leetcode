# 第 407 场周赛 第 1 题
# 题目：100372. 使两个整数相等的位更改次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-407/problems/number-of-bit-changes-to-make-two-integers-equal/
# 题库：https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal

"""
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        for i in range(max(n.bit_length(), k.bit_length())):
            a, b = n >> i & 1, k >> i & 1
            if a == 1 and b == 0:
                ans += 1
            elif a == 0 and b == 1:
                return -1
        return ans
"""


class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k:  # n 不能变为 k
            return -1
        return (n ^ k).bit_count()


s = Solution()
examples = [
    (dict(n=13, k=4), 2),
    (dict(n=21, k=21), 0),
    (dict(n=14, k=13), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minChanges(**e))
