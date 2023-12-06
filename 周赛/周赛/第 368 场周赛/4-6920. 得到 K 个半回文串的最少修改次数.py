from functools import cache
from typing import List
from collections import *
from itertools import *
from math import *

# 题目：6920. 得到 K 个半回文串的最少修改次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-368/problems/minimum-changes-to-make-k-semi-palindromes/
# 题库：https://leetcode.cn/problems/minimum-changes-to-make-k-semi-palindromes/submissions/

# 计算200以内所有数的真因子
# 复杂度计算
# 语句执行的次数：Mx + MX/2 + MX/3 + ... + MX/MX
# MX(1+1/2+1/3+...) 调和级数
# O(MXlogMX)
# 自然数 n 平均有 log n个真因子
# 最坏情况下，有 pow(n,1/3) 个
MX = 201
divisors = [[] for _ in range(MX)]
for i in range(1, MX // 2 + 1):  # [1,100]就行
    for j in range(i * 2, MX, i):  # i不是i的真因子，所以从2*i开始，i是j的真因子
        divisors[j].append(i)


# 时间复杂度 O(nlogn)
# 外层d循环 logn
# 内层的双循环，一共经历 n
# 所以一共 是O(nlogn)
def get_modify(s: str) -> int:
    # 计算将 s 变为为半回文串的最少修改次数
    n = len(s)  # s长度
    res = inf
    for d in divisors[n]:  # 遍历 s长度 的所有真因子
        c = 0  # 计算要修改几个字符。因为要所有 下标%d==0 ， 所以初始化 c=0 放在i循环外面
        for i in range(d):  # 遍历起点
            t = s[i::d]  # 取出 同余为d的下标 的切片
            for j in range(len(t) // 2):
                c += t[j] != t[-j - 1]
        res = min(res, c)
    return res


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        # 半回文串的长度至少为2
        # 因为，1没有真因子，所以长度为1的字符串没有题目中的 d ，所以也就不能是半回文串

        n = len(s)
        # modify[i][j] 表示s[i:j+1](i到j包括j）最少修改多少字符变为半回文串
        modify = [[0] * n for _ in range(n)]
        # 时间复杂度：O(n^2*nlogn) = O(n^3logn)
        for i in range(n - 1):
            for j in range(i + 1, n):  # (n-1)和(i+1,n) 因为长度至少为2
                modify[i][j] = get_modify(s[i:j + 1])

        # dfs(i,j)
        # ## 定义
        # i:划分 i 次，也就是划分成 i+1 个字符串
        # j:s[0] 到 s[j](包括） (s[0:j+1])
        # 返回将 s[0] 到 s[j] 划分成 i+1 个字符串每个字符串都是半回文串的最少修改次数
        # ## 递归入口
        # dfs(k-1,n-1)
        # 划分k组，j从n-1开始
        # ## 状态转移
        # 枚举 L，用 dfs(i-1,L-1) + modify[L][j] 的最小值更新 dfs(i,j)
        # 将 s[:j+1] 划分成 [:L] 和 [L:j+1] 两部分
        # [:L] 进入下一次递归（划分次数少1），[L:j+1]从 modify 数组中获取需要修改的最少次数
        # ### L的范围 [2*i,j-1]
        # 前面还要划分i次，所以前面要有 2*i 个字符，所以 L 的最小值是 2*i
        # 半回文串最小长度是2，当前的末尾下标是 j，所以 L 的最大值是 j-1
        # ## 递归出口 i=0
        # 不需要再划分了，也就是 modify[0][j]
        # ## 时间复杂度：O(kn*n)

        # 记忆化搜索 ###########################################################################
        # @cache
        # def dfs(i, j):
        #     if i == 0:
        #         return modify[0][j]
        #     res = inf
        #     for L in range(2 * i, j):
        #         res = min(res, dfs(i - 1, L - 1) + modify[L][j])
        #     return res
        #
        # return dfs(k - 1, n - 1)

        # 递推形式 ###########################################################################
        # f[i][j] ，划分 i 次，s[0]到s[j]需要修改的最少次数
        # f = [[0] * n for _ in range(k)]
        # f[0] = modify[0]
        # for i in range(1, k):
        #     for j in range(2 * i + 1, n):  # range(2 * i, n) 也行
        #         res = inf
        #         for L in range(2 * i, j):
        #             res = min(res, f[i - 1][L - 1] + modify[L][j])
        #         f[i][j] = res
        # return f[-1][-1]

        # 递推一行形式 ###########################################################################
        f = modify[0]
        for i in range(1, k):
            for j in range(n - 1, 2 * i, -1):
                res = inf
                for L in range(2 * i, j):
                    res = min(res, f[L - 1] + modify[L][j])
                f[j] = res
        return f[-1]


s = Solution()
examples = [
    (dict(s="abcac", k=2), 1),
    (dict(s="abcdef", k=2), 2),
    (dict(s="aabbaa", k=3), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minimumChanges(**e))
