# 第 397 场周赛 第 4 题
# 题目：100312. 找出分数最低的排列
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-397/problems/find-the-minimum-cost-array-permutation/
# 题库：https://leetcode.cn/problems/find-the-minimum-cost-array-permutation

from functools import *
from math import inf
from typing import List


# 1. 第一个位置填 0 就可以
# 2. 构造排列的时候有没重复计算的子问题？
#       从左往右填，要知道前面已经选了哪些数字，以及上一个填的是什么
# 3. 如何构造答案数组？
#       make_ans 函数
# 灵神视频： https://www.bilibili.com/video/BV1bx4y1i7rP/?spm_id_from=333.999.0.0&vd_source=16586319d2fce84d328b49945668eb44
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        @cache
        def dfs(i: int, j: int) -> int:
            if i == (1 << n) - 1:  # 所有数都选完了
                # 最后一个填的是 j 也就是 perm[-1]
                return abs(j - nums[0])
            res = inf
            for k in range(n):  # 遍历填当前这一位
                if i & (1 << k):  # k 已经被填过了
                    continue
                # 填入 k ，并计算填入 k 增加的分数
                t = dfs(i | 1 << k, k) + abs(j - nums[k])
                res = min(res, t)
            return res

        def make_ans(i: int, j: int) -> None:
            ans.append(j)  # 填入答案
            if i == (1 << n) - 1:  # 所有数都选完了
                return
            for k in range(n):  # 遍历填当前这一位
                if i & (1 << k):  # k 已经被填过了
                    continue
                # 填入 k ，并计算填入 k 增加的分数
                t = dfs(i | 1 << k, k) + abs(j - nums[k])
                if t == dfs(i, j):
                    make_ans(i | 1 << k, k)
                    break

        n = len(nums)
        # 第一个位置填 0 ，i=1 表示 {0} 第一个位置填了 0
        dfs(1, 0)

        ans = []
        make_ans(1, 0)
        return ans


# 递推
# f[i][j] = f[i | 1 << k][k] + abs(j - nums[k])
# i 从大到小
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = [[inf] * n for _ in range(1 << n)]
        frm = [[-1] * n for _ in range(1 << n)]  # 记录来源
        # 翻译递归出口
        for j in range(n):
            f[-1][j] = abs(j - nums[0])

        for i in range((1 << n) - 2, 0, -1):  # 递归入口是 i=1 的时候
            for j in range(n):
                if (i >> j) & 1 == 0:  # j 不在 i 里是不对的
                    continue
                res = inf
                for k in range(n):
                    if (i >> k) & 1:
                        continue
                    t = f[i | 1 << k][k] + abs(j - nums[k])
                    if t < res:
                        frm[i][j] = k  # 已经有 i 且上一个填的是 j 的下一个是 k
                        res = t
                f[i][j] = res

        ans = []
        i = j = 0
        while j >= 0:
            ans.append(j)
            i |= 1 << j  # j 填入到 i中
            j = frm[i][j]  # 下一个
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 0, 2]), [0, 1, 2]),
    (dict(nums=[0, 2, 1]), [0, 2, 1]),
]
for e, a in examples:
    print(a, e)
    print(s.findPermutation(**e))
