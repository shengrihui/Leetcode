# 第 406 场周赛 第 1 题
# 题目：100352. 交换后字典序最小的字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-406/problems/lexicographically-smallest-string-after-a-swap/
# 题库：https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap


class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s) - 1):
            a, b = int(s[i]), int(s[i + 1])
            if a > b and a % 2 == b % 2:
                s[i], s[i + 1] = s[i + 1], s[i]
                break
        return "".join(s)


s = Solution()
examples = [
    (dict(s="45320"), "43520"),
    (dict(s="001"), "001"),
]
for e, a in examples:
    print(a, e)
    print(s.getSmallestString(**e))
