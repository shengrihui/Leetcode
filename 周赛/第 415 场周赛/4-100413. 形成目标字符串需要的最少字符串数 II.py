# 第 415 场周赛 第 4 题
# 题目：100413. 形成目标字符串需要的最少字符串数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-ii/
# 题库：https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii

from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        pass


s = Solution()
examples = [
    (dict(words=["abc", "aaaaa", "bcdef"], target="aabcdabc"), 3),
    (dict(words=["abababab", "ab"], target="ababaababa"), 2),
    (dict(words=["abcdef"], target="xyz"), -1),
]
for e, a in examples:
    print(a, e)
    print(s.minValidStrings(**e))
