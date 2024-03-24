# 第 390 场周赛 第 4 题
# 题目：100268. 最长公共后缀查询
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-390/problems/longest-common-suffix-queries/
# 题库：https://leetcode.cn/problems/longest-common-suffix-queries

from math import inf
from typing import List


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        i_len = [(i, len(w)) for i, w in enumerate(wordsContainer)]
        i_len.sort(key=lambda x: (x[1], x[0]))
        son = [[[-1] * 26, i_len[0][1], i_len[0][0]]]  # son[p] 后缀到此的最短字符串长度和下标
        f = lambda ch: ord(ch) - ord("a")
        for i, word in enumerate(wordsContainer):
            p = 0
            length = len(word)
            for c in word[::-1]:
                if son[p][0][f(c)] == -1:
                    son.append([[-1] * 26, inf, -1])
                    son[p][0][f(c)] = len(son) - 1
                    p = len(son) - 1
                else:
                    p = son[p][0][f(c)]
                if son[p][1] > length:
                    son[p][1] = length
                    son[p][2] = i
        ans = []
        for word in wordsQuery:
            p = 0
            for c in word[::-1]:
                if son[p][0][f(c)] == -1:
                    break
                p = son[p][0][f(c)]
            ans.append(son[p][2])
        return ans


# 超内存
"""
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n, qn = len(wordsContainer), len(wordsQuery)
        a = [(i, len(w)) for i, w in enumerate(wordsContainer)]
        a.sort(key=lambda x: (x[1], x[0]))
        x = a[0][0]
        son = [[[-1, []] for _ in range(27)]]
        f = lambda ch: ord(ch) - ord("a")
        for i, word in enumerate(wordsContainer):
            #print(word)
            p = 0
            for c in word[::-1]:
                # print(p, f(c))
                # print(son[p][f(c)][0], sep="\n")
                if son[p][f(c)][0] == -1:
                    son.append([[-1, []] for _ in range(27)])
                    son[p][f(c)][0] = len(son) - 1
                    son[p][f(c)][1].append(i)
                    p = len(son) - 1
                else:
                    son[p][f(c)][1].append(i)
                    p = son[p][f(c)][0]
        #print(*son, sep="\n")
        ans = []
        for word in wordsQuery:
            p = 0
            #print(word)
            idx = []
            for c in word[::-1]:
                if son[p][f(c)][0] == -1:
                    break
                else:
                    idx = son[p][f(c)][1]
                    p = son[p][f(c)][0]
            if idx:
                #print(idx)
                tt = [(i, len(wordsContainer[i])) for i in idx]
                tt.sort(key=lambda x: (x[1], x[0]))
                #print(tt)
                ans.append(tt[0][0])
            else:
                ans.append(x)
        return ans
"""

s = Solution()
examples = [
    (dict(wordsContainer=["a", "b"], wordsQuery=["a", "b"]), [0, 1]),
    (dict(wordsContainer=["abcd", "bcd", "xbcd"], wordsQuery=["cd", "bcd", "xyz"]), [1, 1, 1]),
    (dict(wordsContainer=["abcdefgh", "poiuygh", "ghghgh"], wordsQuery=["gh", "acbfgh", "acbfegh"]), [2, 0, 2]),
]
for e, a in examples:
    print(a, e)
    print(s.stringIndices(**e))
