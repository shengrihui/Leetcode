# 第 416 场周赛 第 2 题
# 题目：100363. 移山所需的最少秒数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-416/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
# 题库：https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero

import heapq
from heapq import *
from math import sqrt
from typing import List


# 堆 ############################################################################################################
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = [(t, 1, t) for t in workerTimes]
        heapq.heapify(h)
        # (如果现在选这个工人要的时间, 这一次之后这个工人下降了的高度, 工人的基本时间)
        for _ in range(mountainHeight):
            t, x, base = heapq.heappop(h)
            heapq.heappush(h, (base * (x + 2) * (x + 1) // 2, x + 1, base))
        # 工人下降的高度 w[i] - 1 等差数列求和然后计算每个工人的总时间
        return max((w[1] - 1) * w[1] // 2 * w[2] for w in h)


# 0x3f
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = [(t, t, t) for t in workerTimes]
        heapify(h)
        for _ in range(mountainHeight):
            # 工作后总用时，当前工作（山高度降低 1）用时，workerTimes[i]
            nxt, delta, base = h[0]
            heapreplace(h, (nxt + delta + base, delta + base, base))
        return max(nxt - delta for nxt, delta, _ in h)


# 二分 ############################################################################################################
# 时间越多，工人能降低的山的高度月大
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(m: int) -> bool:
            # 一共用 m 的时间，能否降低山
            left_h = mountainHeight  # 剩余高度
            for t in workerTimes:
                # 每个工人降低 x 高度，用 m 总时间
                # t * (x+1)*x//2 <= m
                # x(x+1) <= 2m//t
                x = int((-1 + sqrt(1 + 8 * m // t)) / 2)
                left_h -= x
                if left_h <= 0:
                    return True
            return False

        # workerTimes.sort()
        left = 0
        # right = 10 ** 18
        # 假设所有人都是最大的时间 mx
        # 每个人需要下降 x = H // n + 1
        # 总时间 mx * x*(x+1)//2
        mx = max(workerTimes)
        x = mountainHeight // len(workerTimes) + 1
        right = mx * x * (x + 1) // 2
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right


s = Solution()
examples = [
    (dict(mountainHeight=5, workerTimes=[1, 5]), 10),
    (dict(mountainHeight=4, workerTimes=[2, 1, 1]), 3),
    (dict(mountainHeight=10, workerTimes=[3, 2, 2, 4]), 12),
    (dict(mountainHeight=5, workerTimes=[1]), 15),
]
for e, a in examples:
    print(a, e)
    print(s.minNumberOfSeconds(**e))
