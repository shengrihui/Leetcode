from functools import cache
from typing import List


# 题目：100077. 最长相邻不相等子序列 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-115/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def is_ok(s1, s2):
            if len(s1) != len(s2):
                return False
            c = 0
            for x, y in zip(s1, s2):
                if x != y:
                    if c == 1:
                        return False
                    c += 1
            return True

        @cache
        def dfs(start):
            indies = [start]
            i = start + 1
            mx_extend = []
            mx_len_extend = 0
            while i < n:
                if groups[i] != groups[start]:
                    s1, s2 = words[i], words[start]
                    # print(s1,s2,is_ok(s1,s2))
                    if is_ok(s1, s2):
                        extend_indies = dfs(i)
                        if len(extend_indies) > mx_len_extend:
                            mx_len_extend = len(extend_indies)
                            mx_extend = extend_indies
                i += 1
            indies.extend(mx_extend)
            # print(start, indies)
            return indies

        max_indies = []
        max_len = 0
        for i in range(n):
            if i + max_len >= n:
                break
            indies = dfs(i)
            # print(i, indies)
            if len(indies) > max_len:
                max_len = len(indies)
                max_indies = indies

        return [words[i] for i in max_indies]


s = Solution()
examples = [
    (dict(n=3, words=["bab", "dab", "cab"], groups=[1, 2, 2]), ["bab", "cab"]),
    (dict(n=3, words=["bdb", "aaa", "ada"], groups=[2, 1, 3]), ["aaa", "ada"]),
    (dict(n=3, words=["aab", "ca", "cbd"], groups=[3, 3, 2]), ["cbd"]),
    (dict(n=4, words=["a", "b", "c", "d"], groups=[1, 2, 3, 4]), ["a", "b", "c", "d"]),
    (dict(n=9, words=["bad", "dc", "bc", "ccd", "dd", "da", "cad", "dba", "aba"], groups=[9, 7, 1, 2, 6, 8, 3, 7, 2]),
     ["dc", "dd", "da"]),
]
for e, a in examples:
    print(a, e)
    print(s.getWordsInLongestSubsequence(**e))
