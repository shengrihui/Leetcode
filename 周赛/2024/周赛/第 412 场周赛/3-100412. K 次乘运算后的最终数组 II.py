# 第 412 场周赛 第 3 题
# 题目：100412. K 次乘运算后的最终数组 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-412/problems/final-array-state-after-k-multiplication-operations-ii/
# 题库：https://leetcode.cn/problems/final-array-state-after-k-multiplication-operations-ii

import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        MOD = 10 ** 9 + 7
        if multiplier == 1:
            return nums
        mx = max(nums)
        h = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(h)
        while k and h[0][0] < mx:  # 让 mx 变成堆顶
            heapq.heapreplace(h, (h[0][0] * multiplier, h[0][1]))
            k -= 1
        h.sort()
        k, r = divmod(k, len(nums))
        # 排序后前 r 个乘 k//n+1 个，其余乘 k//n 个
        for i, (x, j) in enumerate(h):
            nums[j] = x * pow(multiplier, k + (i < r), MOD) % MOD
        return nums


s = Solution()
examples = [

    (dict(nums=[66307295, 441787703, 589039035, 322281864], k=900900704, multiplier=641725), [125, 375]),
    (dict(nums=[5, 3], k=5, multiplier=5), [125, 375]),
    (dict(nums=[2, 3, 4, 1, 1, 1, 5], k=4, multiplier=2), [4, 3, 4, 2, 2, 2, 5]),
    (dict(nums=[2, 1, 3, 5, 6], k=5, multiplier=2), [8, 4, 6, 5, 6]),
    (dict(nums=[1, 2], k=3, multiplier=4), [16, 8]),
    (dict(nums=[2, 1], k=1, multiplier=2), [2, 2]),
    (dict(nums=[3, 9, 27, 81], k=10, multiplier=3), [243, 243, 243, 243]),
]
for e, a in examples:
    print(a, e)
    print(s.getFinalState(**e))
