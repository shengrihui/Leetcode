# 第 140 场双周赛 第 4 题
# 题目：100433. 第一个几乎相等子字符串的下标
# 题目链接：
# 竞赛：https://leetcode.cn/contest/biweekly-contest-140/problems/find-the-occurrence-of-first-almost-equal-substring/
# 题库：https://leetcode.cn/problems/find-the-occurrence-of-first-almost-equal-substring


class Solution:
    def Z(self, s):
        n = len(s)
        z = [0] * n
        left, right = 0, 0
        for i in range(1, n):
            if i <= right:
                a, b = z[i - left], right - i + 1
                if a < b:
                    z[i] = a
                    continue
                z[i] = b
                # z[i] = min(z[i - left], right - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                left, right = i, (right if right > i + z[i] else i + z[i])
                z[i] += 1
        return z

    def minStartingIndex(self, s: str, pattern: str) -> int:
        # pre_z[m+i] 表示 s 从 s[i] 开始往后有 pre_z[m+i] 个字母和 pattern 的前缀相同
        # suf_z[i](reverse了） 表示 s 从 s[i] 开始往前有 suf_z[i] 个字母和 pattern 的后缀相同
        # pre_z[i] + suf_z[i-m+m-1] >= m-1 就成了
        #           i-m+m-1: i-m 去掉前面的 pattern 对应到 s 的下标，+m 是子串长度，-1 在 suf_z 的下标
        #           >= m-1 : 可以修改一个，所以两个加起来 >= m-1 就行
        #                       修改 k 个就 m-k
        pre_z = self.Z(pattern + s)
        suf_z = self.Z(pattern[::-1] + s[::-1])
        suf_z.reverse()
        m = len(pattern)
        # pre_z 要 [m:]
        # suf_z 要 [:-1-m] = [:s+1]
        # 交集一下 range(m,s+1)
        for i in range(m, len(s) + 1):
            if pre_z[i] + suf_z[i - 1] >= m - 1:
                return i - m
        return -1


s = Solution()
examples = [
    (dict(s="abcdefg", pattern="bcdffg"), 1),
    (dict(s="ababbababa", pattern="bacaba"), 4),
    (dict(s="abcd", pattern="dba"), -1),
    (dict(s="dde", pattern="d"), 0),
]
for e, a in examples:
    print(a, e)
    print(s.minStartingIndex(**e))
