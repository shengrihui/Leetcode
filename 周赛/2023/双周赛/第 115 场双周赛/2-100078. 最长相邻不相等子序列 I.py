from typing import List


# 题目：100078. 最长相邻不相等子序列 I
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-115/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        indies = [0]
        i = 1
        while i < n:
            if groups[i] != groups[indies[-1]]:
                indies.append(i)
            i += 1
        return [words[i] for i in indies]


s = Solution()
examples = [
    (dict(n=3, words=["e", "a", "b"], groups=[0, 0, 1]), ["e", "b"]),
    (dict(n=4, words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]), ["a", "b", "c"]),
]
for e, a in examples:
    print(a, e)
    print(s.getWordsInLongestSubsequence(**e))
