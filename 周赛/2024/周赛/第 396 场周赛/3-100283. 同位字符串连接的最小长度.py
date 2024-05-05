# 第 396 场周赛 第 3 题
# 题目：100283. 同位字符串连接的最小长度
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-396/problems/minimum-length-of-anagram-concatenation/
# 题库：https://leetcode.cn/problems/minimum-length-of-anagram-concatenation
from collections import Counter


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        # for t_len in range(1, n + 1):
        for t_len in range(1, n // 2 + 1):
            if n % t_len != 0:
                continue
            cnt = Counter(s[:t_len])
            for i in range(t_len, n, t_len):
                cnt_t = Counter(s[i:i + t_len])
                # if not all(cnt[c] == cnt_t[c] for c in cnt):
                if not cnt != cnt_t:
                    break
            else:
                return t_len
        return n


s = Solution()
examples = [
    (dict(s="abba"), 2),
    (dict(s="cdef"), 4),
]
for e, a in examples:
    print(a, e)
    print(s.minAnagramLength(**e))
