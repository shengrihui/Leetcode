# 题目：100154. 执行操作后的最大分割数量
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-379/problems/maximize-the-number-of-partitions-after-operations/
# 题库：https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations
from functools import cache


# 记忆化搜索 #############################################################################################################
# dfs(i,mask,changed) 表示遍历到了 s[i],前面的字符集合是 mask 是否（changed）有字符修改过的情况下，
# 从 mask 这一段（开始记录 mask 的地方开始到 s[i-1]）到最后可以分割的数量
# 分类讨论
# 如果前面修改过（changed = True），那 s[i] 不用考虑修改
#   如果 s[i] ∪ mask 的字符数量大于 k ，这里要分割，dfs(i, mask, True) = dfs(i + 1, s[i], True) + 1
#   如果 s[i] ∪ mask 的字符数小于等于 k ，分割数量转移来不增加，，dfs(i, mask, True) = dfs(i + 1, s[i] | mask, True)
# 如果前面修改过（changed = False），那 s[i] 就要考虑修改成其他字符的情况
#   枚举 s[i] 要修改成的字符 c 
#       如果 c ∪ mask 的字符数量大于 k ，这里要分割，dfs(i, mask, False) = dfs(i + 1, c, True) + 1
#       如果 c ∪ mask 的字符数小于等于 k ，分割数量转移来不增加，，dfs(i, mask, False) = dfs(i + 1, c | mask, True)
#   对所有情况取 max
#
# 递归边界：dfs(n,*,*) = 1
# 递归入口：dfs(0,0,False) 即答案
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i: int, mask: int, changed: bool) -> int:
            if i == len(s):
                return 1
            si = ord(s[i]) - ord('a')
            bit = 1 << si  # s[i] 的二进制表示
            new_mask = mask | bit
            if new_mask.bit_count() > k:
                res = dfs(i + 1, bit, changed) + 1
            else:
                res = dfs(i + 1, new_mask, changed)
            if changed:  # 如果前面修改过，直接返回不要考虑修改 s[i]
                return res
            for j in st:
                bit = 1 << j
                new_mask = mask | bit
                if new_mask.bit_count() > k:
                    res = max(res, dfs(i + 1, bit, True) + 1)
                else:
                    res = max(res, dfs(i + 1, new_mask, True))
            return res

        st = set(ord(c) - ord('a') for c in set(s))
        for i in range(26):
            if i not in st:
                st.add(i)
                break
        return dfs(0, 0, False)


# 前后缀分解 #############################################################################################################
"""
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1

        seg, mask, size = 1, 0, 0
        def update(i: int) -> None:
            nonlocal seg, mask, size
            bit = 1 << (ord(s[i]) - ord('a'))
            if mask & bit:
                return
            size += 1
            if size > k:
                seg += 1  # s[i] 在新的一段中
                mask = bit
                size = 1
            else:
                mask |= bit

        n = len(s)
        suf = [None] * n + [(0, 0)]
        for i in range(n - 1, -1, -1):
            update(i)
            suf[i] = (seg, mask)

        ans = seg  # 不修改任何字母
        seg, mask, size = 1, 0, 0
        for i in range(n):
            suf_seg, suf_mask = suf[i + 1]
            res = seg + suf_seg  # 情况 3
            union_size = (mask | suf_mask).bit_count()
            if union_size < k:
                res -= 1  # 情况 1
            elif union_size < 26 and size == k and suf_mask.bit_count() == k:
                res += 1  # 情况 2
            ans = max(ans, res)
            update(i)
        return ans
"""
s = Solution()
examples = [
    (dict(s="acbca", k=2), 3),
    (dict(s="aabaab", k=3), 1),
    (dict(s="xxyz", k=1), 4),
]
for e, a in examples:
    print(a, e)
    print(s.maxPartitionsAfterOperations(**e))
