# 第 389 场周赛 第 3 题
# 题目：100255. 成为 K 特殊字符串需要删除的最少字符数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-389/problems/minimum-deletions-to-make-string-k-special/
# 题库：https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special

from collections import *

# 方法一
# O(n+26n)
"""
letters = "abcdefghijklmnopqrstuvwxyz"


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        n = len(word)
        ans = n
        # 遍历字母可能出现的次数
        # 作为最小的次数
        for i in range(n + 1):  # 暴力了
            delete = 0
            for c in letters:
                if cnt[c] < i:
                    delete += cnt[c]
                if cnt[c] > i + k:
                    delete += cnt[c] - (i + k)
            ans = min(ans, delete)
        return ans
"""


# 方法二
# O(n+26^2)
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = sorted(Counter(word).values())
        # 比 base + k 大的，变为 base + k
        # 比 base 小的，就不保留
        save = 0  # 记录要保留的数量
        for i, base in enumerate(cnt):
            s = 0
            for c in cnt[i:]:
                s += min(base + k, c)
            save = max(save, s)
        return len(word) - save


s = Solution()
examples = [
    (dict(word="aabcaba", k=0), 3),
    (dict(word="a", k=0), 0),
    (dict(word="dabdcbdcdcd", k=2), 2),
    (dict(word="aaabaaa", k=2), 1),
]
for e, a in examples:
    print(a, e)
    print(s.minimumDeletions(**e))
