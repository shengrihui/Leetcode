# 第 135 场双周赛 第 4 题
# 题目：100341. 网格图操作后的最大分数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-135/problems/maximum-score-from-grid-operations/
# 题库：https://leetcode.cn/problems/maximum-score-from-grid-operations

from functools import *
from itertools import *
from typing import List


# O(n^4) 超时
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        # dfs(j,pre,cur) 
        # 现在考虑第 j 列，cur 个黑格，pre 是第 j+1 列的黑格数
        # j 是下标，cur、pre 是数量，所以在计算在缀合的计算的时候，
        # pre > cur , s = col_sum[j][pre] - col_sum[j][cur]
        @cache
        def dfs(j: int, cur: int, pre: int) -> int:
            if j == 0:
                return col_sum[j][pre] - col_sum[j][cur] if pre > cur else 0
            res = 0
            # 枚举 j-1 列的黑格数量
            for nxt in range(n + 1):
                # 计算 j-1 列有 nxt 个黑格，j 列有 cur 个黑格，j+1 列有 pre 个黑格的情况下，j 列有多少分
                mx = nxt if nxt > pre else pre  # nxt 和 pre 的较大值
                s = col_sum[j][mx] - col_sum[j][cur] if mx > cur else 0
                res = max(res, dfs(j - 1, nxt, cur) + s)
            return res

        # 枚举 n-1 列黑格的数量
        return max(dfs(n - 1, i, 0) for i in range(n + 1))


# O(n^3)
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        # dfs(j,pre,dec)
        # 第 j 列，第 j+1 列有 pre 个黑格，若第 j+1 列的黑格数 >= 第 j+2 列的黑格数，dec=Flase
        # 只有第 j+1 列的黑格数 <= 第 j+2 列的黑格数，dec=True
        @cache
        def dfs(j: int, pre: int, dec: bool) -> int:
            if j < 0:  # j=0 的时候还有分呢
                return 0
            res = 0
            # 枚举 j 列的黑格数量 cur
            for cur in range(n + 1):
                if cur == pre:  # 情况1
                    # j 列没有什么可以加入分的，直接进入 j-1，
                    # 除非 j 列黑格数比 j-1 列黑格书少，那在 j-1 里的情况3和4讨论
                    res = max(res, dfs(j - 1, cur, False))
                elif cur < pre:  # 情况2
                    # 第 j 列的 [cur,pre) 加入总分
                    # 递归到 j-1 的时候 dec=True
                    res = max(res, dfs(j - 1, cur, True) + col_sum[j][pre] - col_sum[j][cur])
                # 下面 cur > pre
                elif not dec:  # 情况3
                    # cur > pre >= 第 j+2 列的黑格数
                    # 第 j+1 列 [pre,cur) 加入总分
                    res = max(res, dfs(j - 1, cur, False) + col_sum[j + 1][cur] - col_sum[j + 1][pre])
                # cur > pre < 第 j+2 列的黑格数，凹形
                # 鳄梨直接 else 也行
                # 但凹形的话，pre=0 最优，所以不用考虑其他值，
                # 而 pre < 第 j+2 列的黑格数，在 j+1 的情况2 计算过，
                # 因此这里直接递归到 j-1 不用加 j+1 的值
                elif pre == 0:  # 情况4
                    res = max(res, dfs(j - 1, cur, False))
            return res

        # 枚举 n-1 列黑格的数量
        return max(dfs(n - 2, i, False) for i in range(n + 1))


# 翻译成递推
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        # f[j+1][pre][dec] == dfs(j,pre,dec)
        f = [[[0, 0] for pre in range(n + 1)] for j in range(n)]
        # 递归 j 从 n-2 到 -1 一共 n
        # dfs(-1,pre,dec) = 0 = f[0][pre][dec]
        # dfs(0,pre,dec) = f[1][pre][dec] 循环从这开始
        # dfs(n-2,pre,dec) = f[n-1][pre][dec] 循环到这开始 [0,n-2] range(n-1)
        # dfs(j,pre,dec) = f[j+1][pre][dec]
        for j in range(n - 1):
            for pre in range(n + 1):
                for dec in range(2):
                    res = 0
                    for cur in range(n + 1):
                        if cur == pre:  # 情况1
                            res = max(res, f[j][cur][0])
                        elif cur < pre:  # 情况2
                            res = max(res, f[j][cur][1] + col_sum[j][pre] - col_sum[j][cur])
                        elif not dec:  # 情况3
                            res = max(res, f[j][cur][0] + col_sum[j + 1][cur] - col_sum[j + 1][pre])
                        elif pre == 0:  # 情况4
                            res = max(res, f[j][cur][0])
                    f[j + 1][pre][dec] = res
        return max(f[n - 1][i][0] for i in range(n + 1))


# 时间优化
"""
整体上来看，f[j+1][pre][0/1] 是从 f[j][cur][0/1] 转移过来的
f[j+1][pre][0/1] 的计算通过遍历 cur 并根绝 cur 与 pre 的关系等得到最大的 res 并更新 [j+1][pre][0/1]
现在要去掉 cur 这一层的循环

4种情况有点多~先少考虑一点儿~
（不考虑题目意思了，只看代码的转移）
1. 情况 4 可以直接 else ，elif pre==0 只是这样最优可以不用考虑其他的，但考虑了也不影响结果
2. 情况 1 可以和情况 3 和 4 合并
因此现在变成了
if cur < pre:  # 情况2
    res = max(res, f[j][cur][1] + col_sum[j][pre] - col_sum[j][cur])
elif not dec:  # 情况3
    res = max(res, f[j][cur][0] + col_sum[j + 1][cur] - col_sum[j + 1][pre])
else:  # 情况4
    res = max(res, f[j][cur][0])
res 换成 f[j + 1][pre][dec]

发现：
1. cur < pre 的时候，无论 dec 都进入情况2
        f[j + 1][pre][dec] = max(f[j + 1][pre][dec], f[j][cur][1] + col_sum[j][pre] - col_sum[j][cur])
    即要找 cur 在 [0,pre) 范围内 f[j][cur][1] - col_sum[j][cur] 的最大值
    因为现在目的是要去掉 cur 循环，所以可以在 从小到大枚举pre 的时候用 pre_max 来维护
    式子变成：
        f[j + 1][pre][dec] = max(f[j + 1][pre][dec], pre_max + col_sum[j][pre])
2. cur >= pre 的时候，
    2.1 dec 为 0 进入情况3
            f[j + 1][pre][0] = max(f[j + 1][pre][0], f[j][cur][0] + col_sum[j + 1][cur] - col_sum[j + 1][pre])
        即要找 cur 在 [pre,n] 范围内 f[j][cur][0] + col_sum[j + 1][cur] 的最大值
        因为现在目的是要去掉 cur 循环，所以可以在 从大到小枚举pre 的时候用 suf_max 来维护
        式子变成：
            f[j + 1][pre][0] = max(f[j + 1][pre][0], suf_max - col_sum[j + 1][pre])
    2.2 dec 为 1 进入情况4
            f[j + 1][pre][1] = max(f[j + 1][pre][1], f[j][cur][0])
        类似前面的操作，在 从大到小枚举pre 的时候用 suf_max2 来维护 f[j][cur][0] 在 [pre,n] 范围内的最大值
        式子变成：
            f[j + 1][pre][1] = max(f[j + 1][pre][1], suf_max2)

这下就没有 cur 循环啦
"""


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]
        f = [[[0, 0] for pre in range(n + 1)] for j in range(n)]
        for j in range(n - 1):
            pre_max = f[j][0][1] - col_sum[j][0]
            for pre in range(1, n + 1):
                f[j + 1][pre][0] = max(f[j + 1][pre][0], pre_max + col_sum[j][pre])
                f[j + 1][pre][1] = max(f[j + 1][pre][1], pre_max + col_sum[j][pre])
                pre_max = max(pre_max, f[j][pre][1] - col_sum[j][pre])
            suf_max = suf_max2 = 0
            for pre in range(n, -1, -1):  # 因为要算 [pre,n] 范围内的最大值，所以要先求 max
                suf_max = max(suf_max, f[j][pre][0] + col_sum[j + 1][pre])
                suf_max2 = max(suf_max2, f[j][pre][0])
                f[j + 1][pre][0] = max(f[j + 1][pre][0], suf_max - col_sum[j + 1][pre])
                f[j + 1][pre][1] = max(f[j + 1][pre][1], suf_max2)
        return max(f[n - 1][i][0] for i in range(n + 1))


# 空间优化
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]
        f = [[[0, 0] for pre in range(n + 1)] for j in range(2)]
        for j in range(n - 1):
            jj, new_j = j % 2, 1 - j % 2
            pre_max = f[jj][0][1] - col_sum[jj][0]
            for pre in range(1, n + 1):
                f[new_j][pre][0] = max(f[new_j][pre][0], pre_max + col_sum[j][pre])
                f[new_j][pre][1] = max(f[new_j][pre][1], pre_max + col_sum[j][pre])
                pre_max = max(pre_max, f[jj][pre][1] - col_sum[j][pre])
            suf_max = suf_max2 = 0
            for pre in range(n, -1, -1):
                suf_max = max(suf_max, f[jj][pre][0] + col_sum[j + 1][pre])
                suf_max2 = max(suf_max2, f[jj][pre][0])
                f[new_j][pre][0] = max(f[new_j][pre][0], suf_max - col_sum[j + 1][pre])
                f[new_j][pre][1] = max(f[new_j][pre][1], suf_max2)
        return max(f[(n - 1) % 2][i][0] for i in range(n + 1))


s = Solution()
examples = [
    (dict(grid=[[0, 0, 0, 0, 0], [0, 0, 3, 0, 0], [0, 1, 0, 0, 0], [5, 0, 0, 3, 0], [0, 0, 0, 0, 2]]), 11),
    (dict(grid=[[10, 9, 0, 0, 15], [7, 1, 0, 8, 0], [5, 20, 0, 11, 0], [0, 0, 0, 1, 2], [8, 12, 1, 10, 3]]), 94),
    (dict(grid=[[0, 1, 9, 9, 8], [0, 0, 4, 0, 1], [6, 7, 0, 6, 0], [1, 1, 0, 14, 0], [14, 0, 15, 13, 13]]), 91),
    (dict(grid=[[0, 0, 2, 0], [15, 3, 7, 0], [7, 4, 0, 0], [12, 2, 0, 12]]), 46),
]
for e, a in examples:
    print(a, e)
    print(s.maximumScore(**e))
