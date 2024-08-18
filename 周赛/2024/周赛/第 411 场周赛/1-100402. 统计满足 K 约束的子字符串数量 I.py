# 第 411 场周赛 第 1 题
# 题目：100402. 统计满足 K 约束的子字符串数量 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-411/problems/count-substrings-that-satisfy-k-constraint-i/
# 题库：https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i

from collections import *


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j + 1]
                cnt = Counter(sub)
                if cnt["0"] <= k or cnt["1"] <= k:
                    ans += 1
        return ans


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = left = 0
        cnt = [0, 0]
        for right, c in enumerate(s):
            cnt[ord(c) % 2] += 1
            while cnt[0] > k and cnt[1] > k:  # 不满足条件
                cnt[ord(s[left]) % 2] -= 1
                left += 1
            ans += right - left + 1
        return ans


s = Solution()
examples = [
    (dict(s="10101", k=1), 12),
    (dict(s="1010101", k=2), 25),
    (dict(s="11111", k=1), 15),
]
for e, a in examples:
    print(a, e)
    print(s.countKConstraintSubstrings(**e))
