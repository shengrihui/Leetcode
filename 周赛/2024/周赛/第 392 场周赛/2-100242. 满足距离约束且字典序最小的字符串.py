# 第 392 场周赛 第 2 题
# 题目：100242. 满足距离约束且字典序最小的字符串
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-392/problems/lexicographically-smallest-string-after-operations-with-constraint/
# 题库：https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint


class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        t = list(s)
        n = len(s)
        i = 0
        while k > 0 and i < n:
            c = s[i]
            if c > "n":
                cost = 1 + ord("z") - ord(c)
            else:
                cost = ord(c) - ord("a")
            if cost > k:
                t[i] = chr(ord(c) - k)
                k = 0
            else:
                k -= cost
                t[i] = "a"
            print(k, t)
            i += 1
        return "".join(t)


"""
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        s = list(s)
        for i, c in enumerate(s):
            dis = min(ord(c) - ord('a'), ord('z') - ord(c) + 1)
            if dis > k:
                s[i] = chr(ord(c) - k)
                break
            s[i] = 'a'
            k -= dis
        return ''.join(s)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/solutions/2727203/tan-xin-pythonjavacgo-by-endlesscheng-vzgo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
s = Solution()
examples = [
    (dict(s="rn", k=9), "an"),
    (dict(s="zbbz", k=3), "aaaz"),
    (dict(s="xaxcd", k=4), "aawcd"),
    (dict(s="lol", k=0), "lol"),
]
for e, a in examples:
    print(a, e)
    print(s.getSmallestString(**e))
