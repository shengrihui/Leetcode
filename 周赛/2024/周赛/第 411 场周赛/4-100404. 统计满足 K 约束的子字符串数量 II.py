# 第 411 场周赛 第 4 题
# 题目：100404. 统计满足 K 约束的子字符串数量 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-ii/
# 题库：https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii

import bisect
from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # left[i] 满足条件的、右端点是 i 的子数组的左端点最远可以是几
        # left[i] 是有序的
        left = [0] * n
        l = 0
        cnt = [0, 0]
        pre = [0] * (n + 1)
        for r, c in enumerate(s):
            cnt[ord(c) % 2] += 1
            while cnt[0] > k and cnt[1] > k:  # 不满足条件
                cnt[ord(s[l]) % 2] -= 1
                l += 1
            left[r] = l
            pre[r + 1] += pre[r] + r - l + 1
        ans = []
        # 若 left[r] <= l ，则 [l,r] 之间所有的子串都符合条件，数量是 1 + 2 + ... + l-r+1
        # 若 left[r] > l
        #   设 j 是第一个满足 left[j] >= l , 那么 [l,j-1] 之间所有子串都满足，数量是 1 + 2 + ... + j-l
        #   [j,r] 之间，每一个下标 i 作为右端点符合条件的子串的数量有 i-left[i]+1，前缀和优化
        for l, r in queries:
            j = bisect.bisect_left(left, l, l, r + 1)  # left 的 [l,r+1) 范围内 >= l 的位置
            ans.append((j - l) * (j - l + 1) // 2 + pre[r + 1] - pre[j])
        return ans


s = Solution()
examples = [
    (dict(s="0001111", k=2, queries=[[0, 6]]), [26]),
    (dict(s="010101", k=1, queries=[[0, 5], [1, 4], [2, 3]]), [15, 9, 3]),
]
for e, a in examples:
    print(a, e)
    print(s.countKConstraintSubstrings(**e))
