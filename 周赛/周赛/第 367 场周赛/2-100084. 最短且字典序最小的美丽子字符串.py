from typing import List
from collections import *
from itertools import *


# 题目：100084. 最短且字典序最小的美丽子字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-367/problems/shortest-and-lexicographically-smallest-beautiful-string/
# 题库：https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        indies = [i for i, c in enumerate(s) if c == "1"]
        n = len(indies)
        if n < k:
            return ""
        mn_len = len(s) + 5
        mn_s = s
        for i in range(0, n - k + 1):
            start, end = indies[i], indies[i + k - 1]
            l = end - start + 1
            s_t = s[start:end + 1]
            if l < mn_len:
                mn_len = l
                mn_s = s_t
            elif l == mn_len:
                if mn_s > s_t:
                    mn_s = s_t
        return mn_s


s = Solution()
examples = [
    (dict(s="100011001", k=3), "11001"),
    (dict(s="1011", k=2), "11"),
    (dict(s="000", k=1), ""),
    (dict(s="001110101101101111", k=10), "10101101101111"),
]
for e, a in examples:
    print(a, e)
    print(s.shortestBeautifulSubstring(**e))
