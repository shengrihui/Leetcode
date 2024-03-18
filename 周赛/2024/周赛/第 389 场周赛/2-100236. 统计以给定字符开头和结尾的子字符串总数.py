# 第 389 场周赛 第 2 题
# 题目：100236. 统计以给定字符开头和结尾的子字符串总数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-389/problems/count-substrings-starting-and-ending-with-given-character/
# 题库：https://leetcode.cn/problems/count-substrings-starting-and-ending-with-given-character

from collections import *


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = Counter(s)[c]
        return n * (n + 1) // 2
