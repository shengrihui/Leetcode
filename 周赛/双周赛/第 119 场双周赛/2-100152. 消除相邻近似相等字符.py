# 题目：100152. 消除相邻近似相等字符
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-119/problems/remove-adjacent-almost-equal-characters/
# 题库：https://leetcode.cn/problems/remove-adjacent-almost-equal-characters

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        i = 1
        ans = 0
        while i < n:
            if word[i] == word[i - 1] or abs(ord(word[i]) - ord(word[i - 1])) == 1:
                ans += 1
                i += 1
            i += 1
        return ans


s = Solution()
examples = [
    (dict(word="aaaaa"), 2),
    (dict(word="abddez"), 2),
    (dict(word="zyxyxyz"), 3),
]
for e, a in examples:
    print(a, e)
    print(s.removeAlmostEqualCharacters(**e))
