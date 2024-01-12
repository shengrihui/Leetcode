from typing import List


# 题目：100129. 回文串重新排列查询
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-378/problems/palindrome-rearrangement-queries/
# 题库：https://leetcode.cn/problems/palindrome-rearrangement-queries

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        pass


s = Solution()
examples = [
    (dict(s="abcabc", queries=[[1, 1, 3, 5], [0, 2, 5, 5]]), [true, true]),
    (dict(s="abbcdecbba", queries=[[0, 2, 7, 9]]), [false]),
    (dict(s="acbcab", queries=[[1, 2, 4, 5]]), [true]),
]
for e, a in examples:
    print(a, e)
    print(s.canMakePalindromeQueries(**e))
