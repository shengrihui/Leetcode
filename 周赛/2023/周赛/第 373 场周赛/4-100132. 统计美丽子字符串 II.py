# 题目：100132. 统计美丽子字符串 II 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-373/problems/count-beautiful-substrings-ii/
# 题库：https://leetcode.cn/problems/count-beautiful-substrings-ii
from collections import Counter
from itertools import accumulate

"""
1.
假设子字符串的长度是 L
有 (L/2)^2 % k == 0
也就是 L^2 是 4k 的倍数
假设 L = dx ，L 是 d 的倍数
那么有 d^2 是 4k 的倍数
因为题目 k 的范围比较小，可以枚举 d
这样就将 L^2 是 4k 的倍数转换成了 L 是 d 的倍数

2.
子数组 [i,j) 的长度 L = j - i
(j - i) % d = 0
j % d = i % d

3.
元音字母 = 1，辅音字母 = -1
子数组和 = 0
前缀和 sum( [i,j) ) =  pre_sum[j] - pre_sum[ji] = 0
pre_sum[i] = pre_sum[j]

4.
记录 pair (pre_sum[i] ,i % d)
i 是 pre_sum 的下标

5. 进一步
不需要 pre_sum ，在遍历的同时计算
用分解质因数的芳芳求 d
"""


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        d = 1
        while d * d % (4 * k) != 0:
            d += 1
        pre_sum = list(accumulate([1 if c in "aeiou" else -1 for c in s], initial=0))
        ans = 0
        cnt = Counter()
        for i, x in enumerate(pre_sum):
            p = (x, i % d)
            ans += cnt[p]
            cnt[p] += 1
        return ans


s = Solution()
examples = [
    (dict(s="baeyh", k=2), 2),
    (dict(s="abba", k=1), 3),
    (dict(s="bcdf", k=1), 0),
    (dict(s="eeebjoxxujuaeoqibd", k=8), 4),
]
for e, a in examples:
    print(a, e)
    print(s.beautifulSubstrings(**e))
