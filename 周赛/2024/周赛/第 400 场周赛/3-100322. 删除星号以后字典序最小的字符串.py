# 第 400 场周赛 第 3 题
# 题目：100322. 删除星号以后字典序最小的字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-400/problems/lexicographically-minimum-string-after-removing-stars/
# 题库：https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars


class Solution:
    def clearStars(self, s: str) -> str:
        ans = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == "*":
                for indies in ans:
                    if indies:
                        indies.pop()
                        break
            else:
                ans[ord(c) - 97].append(i)
        t = [(i, chr(o + 97)) for o, indies in enumerate(ans) for i in indies]
        t.sort()
        ans = [c for i, c in t]
        return "".join(ans)


"""
class Solution:
    def clearStars(self, s: str) -> str:
        st = [[] for _ in range(26)]
        delete = [False] * len(s)
        for i, c in enumerate(s):
            if c != "*":
                st[ord(c) - ord("a")].append(i)
                continue
            # 是 *
            delete[i] = True
            for p in st:
                if p:
                    delete[p.pop()] = True
                    break
        return "".join([c for i, (c, d) in enumerate(zip(s, delete)) if not d])
"""

s = Solution()
examples = [
    (dict(s="aaba*"), "aab"),
    (dict(s="abc"), "abc"),
]
for e, a in examples:
    print(a, e)
    print(s.clearStars(**e))
