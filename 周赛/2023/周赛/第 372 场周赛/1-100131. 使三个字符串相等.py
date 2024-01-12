# 题目：100131. 使三个字符串相等
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-372/problems/make-three-strings-equal/
# 题库：https://leetcode.cn/problems/make-three-strings-equal

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        a, b, c = len(s1), len(s2), len(s3)
        mm = min(a, b, c)
        for i in range(mm):
            if s1[i] != s2[i] or s2[i] != s3[i] or s1[i] != s3[i]:
                mm = i
                break
        if mm == 0:
            return -1
        return a + b + c - 3 * mm


s = Solution()
examples = [
    (dict(s1="abc", s2="abb", s3="ab"), 2),
    (dict(s1="dac", s2="bac", s3="cac"), -1),
    (dict(s1="abc", s2="aaa", s3="ab"), -1),
]
for e, a in examples:
    print(a, e)
    print(s.findMinimumOperations(**e))
