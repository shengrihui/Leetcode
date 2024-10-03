# 第 417 场周赛 第 3 题
# 题目：100424. 元音辅音字符串计数 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-417/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/
# 题库：https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        pass


s = Solution()
examples = [
    (dict(word="aeioqq", k=1), 0),
    (dict(word="aeiou", k=0), 1),
    (dict(word="ieaouqqieaouqq", k=1), 3),
]
for e, a in examples:
    print(a, e)
    print(s.countOfSubstrings(**e))
