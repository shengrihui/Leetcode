from typing import List
from collections import *
from itertools import *
from functools import *
from math import *


# 题目：100145. 统计完全子字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-374/problems/count-complete-substrings/
# 题库：https://leetcode.cn/problems/count-complete-substrings

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def f(s: str) -> int:
            # 假设有 m 个字母有 k 个，那子串的长度就是 mk
            res = 0
            for m in range(1, 27):  # 最多26个字母
                size = m * k  # 滑动窗口的大小
                if size > len(s):  # 剪枝，窗口比整个字符串还大
                    break
                cnt = Counter(s[:size])
                res += all(v == k for v in cnt.values())
                for in_c, out in zip(s[size:], s):
                    cnt[in_c] += 1
                    cnt[out] -= 1
                    #       v==0 有可能有些字符在这个窗口里没有，但其他字母都是k个
                    res += all(v == 0 or v == k for v in cnt.values())
            return res

        # 循环分组，按照条件二分成一组一组，每一组再放 f 里算
        ans, i, n = 0, 0, len(word)
        while i < n:
            start = i  # 这一组开始的位置
            i += 1
            while i < n and abs(ord(word[i]) - ord(word[i - 1])) <= 2:
                i += 1
            # i 指向这一组结束的下一个
            ans += f(word[start:i])
        return ans


s = Solution()
examples = [
    (dict(word="igigee", k=2), 3),
    (dict(word="aaabbbccc", k=3), 6),
]
for e, a in examples:
    print(a, e)
    print(s.countCompleteSubstrings(**e))
