# 第 408 场周赛 第 2 题
# 题目：100371. 统计不是特殊数字的数字数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-408/problems/find-the-count-of-numbers-which-are-not-special/
# 题库：https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special

from math import isqrt

n = isqrt(10 ** 9)
st = [False] * (n + 1)  # st[i]有没有被筛过
primes = []
cnt = 0  # 第几个质数
for i in range(2, n + 1):
    if not st[i]:  # 第i个没有被筛掉，说明ta是质数
        cnt += 1
        primes.append(i)

    j = 0
    while primes[j] <= n // i:
        st[primes[j] * i] = True
        # print(i, j, primes[j], primes[j] * i)
        if i % primes[j] == 0:
            break
        j += 1


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ans = 0
        for x in primes:
            if l <= x * x <= r:
                ans += 1
            if x * x > r:
                break
        return r - l + 1 - ans


s = Solution()
examples = [
    (dict(l=5, r=7), 3),
    (dict(l=4, r=16), 11),
]
for e, a in examples:
    print(a, e)
    print(s.nonSpecialCount(**e))
