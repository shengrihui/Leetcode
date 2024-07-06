# 题目：100129. 回文串重新排列查询
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-378/problems/palindrome-rearrangement-queries/
# 题库：https://leetcode.cn/problems/palindrome-rearrangement-queries
from itertools import accumulate
from typing import List


# 53 个前缀和
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s) // 2
        t = s[n:][::-1]  # 后一半再翻转
        s = s[:n]

        # sum_s[i][c]
        # 计算 s 在 [l,r] 各个字符出现的次数：
        # sum_s[r+1][*] - sum_s[l][*]
        sum_s = [[0] * 26 for _ in range(n + 1)]
        for i, c in enumerate(s):
            sum_s[i + 1] = sum_s[i][:]  # 先拷贝一份 i 的
            sum_s[i + 1][ord(c) - 97] += 1  # c 多一个

        sum_t = [[0] * 26 for _ in range(n + 1)]
        for i, c in enumerate(t):
            sum_t[i + 1] = sum_t[i][:]
            sum_t[i + 1][ord(c) - 97] += 1

        # 计算 s,t 对应位置上有多少不一样的的前缀和
        # 计算 s,t 在 [l,r] 上有多少个字符不一样
        # sum_ne[r+1] - sum_ne[l]
        # ne = not equal
        sum_ne = list(accumulate([x != y for x, y in zip(s, t)], initial=0))

        # 计算区间为 [l,r] 的子串各个字符出现的次数
        # pre_sum 是 s 或 t 的前缀和
        # 返回长度 26 的数组
        def count(pre_sum: List[List[int]], l: int, r: int) -> List[int]:
            # pre_sum[r + 1][*] - pre_sum[l][*]
            return [x - y for x, y in zip(pre_sum[r + 1], pre_sum[l])]

        # s1 各个字符的数量减去 s2 中各个子树的数量
        # s1 s2 返回 都是长度 26 的数组
        def subtract(s1: List[int], s2: List[int]) -> List[int]:
            for i, c in enumerate(s2):
                s1[i] -= c
                if s1[i] < 0:  # 可能小于 0 返回空 或者 False
                    return None
            return s1  # 返回“被减数”

        def check(l1: int, r1: int, sumS: List[List[int]], l2: int, r2: int, sumT: List[List[int]]) -> bool:
            # 最左边和最右边有不相同的字符
            if sum_ne[l1] > 0 or sum_ne[-1] - sum_ne[max(r1, r2) + 1] > 0:
                return False
            # 不相交
            if l2 > r1:
                return count(sumS, l1, r1) == count(sumT, l1, r1) and \
                    count(sumS, l2, r2) == count(sumT, l2, r2) and \
                    sum_ne[l2] - sum_ne[r1 + 1] == 0
            # 包含
            if r2 <= r1:
                return count(sumS, l1, r1) == count(sumT, l1, r1)
            # 相交
            s1 = subtract(count(sumS, l1, r1), count(sumT, l1, l2 - 1))
            s2 = subtract(count(sumT, l2, r2), count(sumS, r1 + 1, r2))
            return s1 is not None and s2 is not None and s1 == s2

        ans = []
        for l1, r1, c, d in queries:
            # 将 c,d 对应到后半串字符串翻转后的下标
            l2, r2 = n * 2 - d - 1, n * 2 - c - 1
            if l2 < l1:
                res = check(l2, r2, sum_t, l1, r1, sum_s)
            else:
                res = check(l1, r1, sum_s, l2, r2, sum_t)
            ans.append(res)
        return ans


s = Solution()
examples = [
    (dict(s="abcabc", queries=[[1, 1, 3, 5], [0, 2, 5, 5]]), [True, True]),
    (dict(s="abbcdecbba", queries=[[0, 2, 7, 9]]), [False]),
    (dict(s="acbcab", queries=[[1, 2, 4, 5]]), [True]),
    (dict(s="odaxusaweuasuoeudxwa", queries=[[0, 5, 10, 14]]), [False]),
]
for e, a in examples:
    print(a, e)
    print(s.canMakePalindromeQueries(**e))
