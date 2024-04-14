# 第 393 场周赛 第 3 题
# 题目：100267. 单面值组合的第 K 小金额
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-393/problems/kth-smallest-amount-with-single-denomination-combination/
# 题库：https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination
from math import lcm
from typing import List


# 找第 k 小的数， k 这么大，考虑用二分
# 二分答案，check(m) 判断 m 金额内可不可以获得 k 个数
#
# 容斥原理（通用）
# |A| + |B| - |AB|
# |A| + |B| + |C| - |AB| - |AC| - |BC| + |ABC|
#
# 新加入一个 D，他要与之前的每一个都交集
# 并且符号取反（奇数个正，偶数个负），
# 这是 D 的“贡献”，然后在加上之前 ABC 的
#
# 对 coins 所有计算容斥原理，要算子集
# 有多个数的时候，要算多个数的 lcm
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(m: int):
            cnt = 0
            for i in range(1, 1 << n):  # 枚举子集
                lcm_val = 1
                for j in range(n):
                    if i >> j & 1:
                        lcm_val = lcm(lcm_val, coins[j])
                c = m // lcm_val  # 集合中第 i 个情况的“贡献”
                # 容斥原理里，奇数个集合的交集符号是正的，偶数个符号是负的
                cnt += c if i.bit_count() % 2 else -c
            return cnt >= k

        n = len(coins)
        left, right = k, min(coins) * k
        while left <= right:
            m = (left + right) // 2
            if check(m):  # m 内有 k 种金额
                right = m - 1
            else:
                left = m + 1
        return left


s = Solution()
examples = [
    (dict(coins=[5], k=7), 35),
    (dict(coins=[3, 6, 9], k=3), 9),
    (dict(coins=[5, 2], k=7), 12),
]
for e, a in examples:
    print(a, e)
    print(s.findKthSmallest(**e))
