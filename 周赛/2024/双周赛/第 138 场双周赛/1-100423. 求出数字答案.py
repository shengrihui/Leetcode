# 第 138 场双周赛 第 1 题
# 题目：100423. 求出数字答案
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-138/problems/find-the-key-of-the-numbers/
# 题库：https://leetcode.cn/problems/find-the-key-of-the-numbers


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans = 0
        pow10 = 1
        for i in range(4):
            ans += min(num1 % 10, num3 % 10, num2 % 10) * pow10
            num1 //= 10
            num3 //= 10
            num2 //= 10
            pow10 *= 10
        return ans


s = Solution()
examples = [
    (dict(num1=1, num2=10, num3=1000), 0),
    (dict(num1=987, num2=879, num3=798), 777),
    (dict(num1=1, num2=2, num3=3), 1),
]
for e, a in examples:
    print(a, e)
    print(s.generateKey(**e))
