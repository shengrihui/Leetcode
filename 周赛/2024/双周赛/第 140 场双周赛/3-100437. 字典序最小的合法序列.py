# 第 140 场双周赛 第 3 题
# 题目：100437. 字典序最小的合法序列
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-140/problems/find-the-lexicographically-smallest-valid-sequence/
# 题库：https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence

from typing import List

"""
从特殊到一般：如果不能修改 -> 修改一次

不能修改：双指针匹配

修改一次
枚举 word1 中的字母 word1[i] 作为修改的字母
后缀 
    suf[i] = j 表示 word1[i:] 可以匹配 word2[j:]
前缀 
    能修改就修改
    前缀匹配长度 j + suf[i+1] + 1 >= len(word2) return
"""


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suf = [0] * (n + 1)
        suf[n] = m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = j + 1

        ans = []
        change = False  # 没有修改过
        j = 0
        for i, c in enumerate(word1):
            # 如果相等就直接加入 ans
            # 如果不等
            #   没有修改过，且 suf[i+1] <= j +1 则修改记录 ans
            #       此时 word1[i] 和 word2[j] 不一样，要将 word1[i] 修改成 word2[j]，什么情况下可以修改呢？
            #       word1[i+1:] 要匹配 word2[j+1:] 的
            #       而只要 suf[i+1] <= j+1 即可满足
            if c == word2[j] or not change and suf[i + 1] <= j + 1:
                if c != word2[j]:
                    change = True
                ans.append(i)
                j += 1
                if j == m:
                    return ans
        return []


s = Solution()
examples = [
    (dict(word1="bbeigiibhjafjig", word2="iihhj"), [3, 5, 6, 8, 9]),
    (dict(word1="vbcca", word2="abc"), [0, 1, 2]),
    (dict(word1="bacdc", word2="abc"), [1, 2, 4]),
    (dict(word1="aaaaaa", word2="aaabc"), []),
    (dict(word1="abc", word2="ab"), [0, 1]),
]
for e, a in examples:
    print(a, e)
    print(s.validSequence(**e))
