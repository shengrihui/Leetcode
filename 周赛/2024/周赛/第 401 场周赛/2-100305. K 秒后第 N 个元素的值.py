# 第 401 场周赛 第 2 题
# 题目：100305. K 秒后第 N 个元素的值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-401/problems/find-the-n-th-value-after-k-seconds/
# 题库：https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds

from math import comb

"""
为什么杨辉三角是组合数？

有公式：
C(n,k) = C(n-1,k-1) + C(n-1,k)
解释：
从 n 中选 k 个，等于
1. 最后一个选，从 n-1 中再选 k-1 个
2. 最后一个不选，从 n-1 中再选 k 个

"""


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # MOD = 10 ** 9 + 7
        # a = [1] * n
        # for _ in range(k):
        #     for i in range(1, n):
        #         a[i] += a[i - 1]
        #         a[i] %= MOD
        # return a[-1]
        return comb(k + n - 1, k) % (10 ** 9 + 7)


s = Solution()
examples = [
    (dict(n=4, k=5), 56),
    (dict(n=5, k=3), 35),
]
for e, a in examples:
    print(a, e)
    print(s.valueAfterKSeconds(**e))
