# 第 124 场双周赛 第 2 题
# 题目：100211. 进行操作使字符串为空
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-124/problems/apply-operations-to-make-string-empty/
# 题库：https://leetcode.cn/problems/apply-operations-to-make-string-empty

from collections import *


# 法一
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        l = max([len(v) for v in d.values()])
        ans = []
        for k, v in d.items():
            if len(v) == l:
                ans.append((v[-1], k))
        ans.sort()
        return "".join([c for _, c in ans])


# 法二：灵神
"""
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}  # 最后一次出现的下标
        cnt = Counter(s)
        mx = max(cnt.values())
        ids = sorted(last[ch] for ch, c in cnt.items() if c == mx)
        return ''.join(s[i] for i in ids)
"""
# 法三：时间最优
"""
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        maxcnt = 0
        cnt = []
        for x in range(0, 26):
            a = s.count(chr(x + ord('a')))
            cnt.append(a)
            maxcnt = max(maxcnt, a)
        app = []
        idx = []
        for i in range(0, 26):
            if cnt[i] == maxcnt:
                app.append(i)
        for x in app:
            idx.append((s[::-1].index(chr(x + ord('a'))), chr(x + ord('a'))))
        ans = ''
        idx.sort()
        for (x, y) in idx[::-1]:
            ans += y
        return ans
"""

s = Solution()
examples = [
    (dict(s="aabcbbca"), "ba"),
    (dict(s="abcd"), "abcd"),
]
for e, a in examples:
    print(a, e)
    print(s.lastNonEmptyString(**e))
