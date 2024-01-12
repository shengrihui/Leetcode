# 题目：100119. 最大异或乘积
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-372/problems/maximum-xor-product/
# 题库：https://leetcode.cn/problems/maximum-xor-product

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        ans = 0
        for i in range(n):
            a_bit, b_bit = (a >> i) & 1, (b >> i) & 1
            if a_bit == b_bit:
                ans |= (1 ^ a_bit) << i
                # print(a_bit,b_bit,ans,bin(ans))
            else:
                ans1 = ans | (1 << i)
                if (ans1 ^ a) * (ans1 ^ b) > (ans ^ a) * (ans ^ b):
                    ans = ans1
        return (ans ^ a) * (ans ^ b) % (10 ** 9 + 7)


s = Solution()
examples = [
    (dict(a=12, b=5, n=4), 98),
    (dict(a=6, b=7, n=5), 930),
    (dict(a=1, b=6, n=3), 12),
]
for e, a in examples:
    print(a, e)
    print(s.maximumXorProduct(**e))
