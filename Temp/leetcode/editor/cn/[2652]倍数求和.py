# 2652 倍数求和


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)
        # m = n//3
        # 3+6+...+3m=m(3+3m)//2=3m(1+m)//2
        # s = 0
        # for x in [3, 5, 7, 105]:
        #     m = n // x
        #     s += x * m * (1 + m) // 2
        # for x in [15, 21, 35]:
        #     m = n // x
        #     s -= x * m * (1 + m) // 2
        # return s
        return sum((-1) ** i * x * (n // x) * (1 + n // x) // 2 for i, x in enumerate([3, 15, 5, 35, 7, 21, 105]))
# leetcode submit region end(Prohibit modification and deletion)
