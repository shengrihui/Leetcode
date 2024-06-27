# 第 388 场周赛 第 4 题
# 题目：100216. K 个不相交子数组的最大能量值
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-388/problems/maximum-strength-of-k-disjoint-subarrays/
# 题库：https://leetcode.cn/problems/maximum-strength-of-k-disjoint-subarrays

from itertools import *
from math import inf
from typing import List

"""
f[i][j] 表示 nums[0]` 到 nums[j-1] （j个数） 分成 j 段

考虑 nums[j-1] 选或不选
不选，
    f[i][j] = f[i][j-1] 直接转移
选：  
    nums[j-1] 作为第 i 组的最右元素，枚举最左元素 L，用前缀和计算 sum(nums[L...j-1]) =  s[j] - s[L]
    L 的范围： i-i <= L <= j-1
            [L,j-1] 是第 i 组，L 的左边有 i-1 组需要 i-1 个数，所以 L 最小 i-1
            最大是这一组的最右 j-1，也就是 1 个元素
    f[i][j] = max_{L=i-1}^{j-1}{ f[i-1][L] + (s[j] - s[L]) * w }
            = s[j] * w + max_{L=i-1}^{j-1}{ f[i-1][L] + s[L] * w }
综上：f[i][j] = max(f[i][j-1], s[j] * w + max_{L=i-1}^{j-1}{ f[i-1][L] + s[L] * w })

max_{L=i-1}^{j-1}{ f[i-1][L] + s[L] * w } 只与 L 有关
可以在枚举 j 的时候，用 mx 取维护它这个 max

f[i][j] = max(f[i][j-1], s[j] * w + mx)
w =  (-1)^(i+1) * (k-i+1)

f 的大小 (n+1) * (k+1)
f = [[0] * (n=1) for _ in range(k+1)]
i，j 都从小到大遍历

j<i-1  j 个数分 i-1 组不合法 f[i][j] = -inf  取 max 没了
j 的范围： i <= j < n-k+i+1
    左边要有 i-1 个数分 i-1 组，因为 j 现在是第 i 组，所以 j 最小是 i
    右边要有 k-i 个数分 k-i 组，所以最大是 n-(k-i) 个数

答案：f[k][n]

"""


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))  # 前缀和
        f = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            w = (1 if i % 2 else -1) * (k - i + 1)
            f[i][i - 1] = mx = -inf
            for j in range(i, n - k + i + 1):
                # mx = max(mx, f[i - 1][j - 1] - w * s[j - 1])
                # f[i][j] = max(f[i][j - 1], mx + s[j] * w)
                t = f[i - 1][j - 1] - w * s[j - 1]  # L = j-1
                if t > mx:
                    mx = t
                t = mx + s[j] * w
                f[i][j] = f[i][j - 1] if f[i][j - 1] > t else t
        return f[k][n]


# 空间优化
# 灵神
"""
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        f = [0] * (n + 1)
        for i in range(1, k + 1):
            pre = f[i - 1]
            f[i - 1] = mx = -inf
            w = (k - i + 1) * (1 if i % 2 else -1)
            for j in range(i, n - k + i + 1):
                mx = max(mx, pre - s[j - 1] * w)
                pre = f[j]
                f[j] = max(f[j - 1], s[j] * w + mx)
        return f[n]
"""

s = Solution()
examples = [
    (dict(nums=[24, -20, 52], k=1), 56),
    (dict(nums=[7, -70, 75], k=1), 75),
    (dict(nums=[-100000000, -10000000, 123, 234], k=3), -30000012),
    (dict(nums=[1, 2, 3, -1, 2], k=3), 22),
    (dict(nums=[12, -2, -2, -2, -2], k=5), 64),
    (dict(nums=[-1, -2, -3], k=1), -1),
]
for e, a in examples:
    print(a, e)
    print(s.maximumStrength(**e))
    print()
