# 题目：100184. 找出出现至少三次的最长特殊子字符串 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-378/problems/find-longest-special-substring-that-occurs-thrice-ii/
# 题库：https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii

# cnt[ch][i] 以差分数组的形式记录长为 i 的 ch 字符串的出现次数
"""
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        cnt = [[0] * (n + 2) for _ in range(26)]
        f = lambda c: ord(c) - 97
        i = 0
        while i < n:
            start = i
            ch = f(s[start])
            cnt[ch][2] -= 1
            cnt[ch][0] += 1
            i += 1
            while i < n and s[i] == s[i - 1]:
                cnt[ch][0] += 1
                cnt[ch][i - start + 2] -= 1
                i += 1
        ans = -1
        for ele in cnt:
            t = accumulate(ele, lambda x, y: x + y)
            for i, c in enumerate(t):
                if c >= 3 and i > ans:
                    ans = i
        return ans
"""


# 分类讨论
# 内容相同的特殊子串的长度
# 前三的长度为 L1 L2 L3
# 按这个分类讨论
# 进一步优化： 用堆
# https://www.bilibili.com/video/BV1XG411B7bX/?t=1m44s&vd_source=16586319d2fce84d328b49945668eb44
class Solution:
    def maximumLength(self, s: str) -> int:
        groups = defaultdict(list)
        cnt = 0
        for i, ch in enumerate(s):
            cnt += 1
            if i + 1 == len(s) or ch != s[i + 1]:
                groups[ch].append(cnt)  # 统计连续字符长度
                cnt = 0

        ans = 0
        for a in groups.values():
            a.sort(reverse=True)
            a.extend([0, 0])  # 假设还有两个空串
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

        return ans if ans else -1


s = Solution()
examples = [
    (dict(s="aaaa"), 2),
    (dict(s="abcdef"), -1),
    (dict(s="abcaba"), 1),
]
for e, a in examples:
    print(a, e)
    print(s.maximumLength(**e))
