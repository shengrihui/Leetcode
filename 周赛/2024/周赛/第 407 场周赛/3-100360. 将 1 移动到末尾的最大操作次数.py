# 第 407 场周赛 第 3 题
# 题目：100360. 将 1 移动到末尾的最大操作次数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-407/problems/maximum-number-of-operations-to-move-ones-to-the-end/
# 题库：https://leetcode.cn/problems/maximum-number-of-operations-to-move-ones-to-the-end

# 对的，但太丑了，不优雅
"""
class Solution:
    def maxOperations(self, s: str) -> int:
        c = ans = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "0":
                i += 1
                continue
            st = i
            i += 1
            while i < n and s[i] == "1":
                i += 1
            if i < n:
                c += i - st
                ans += c
        return ans
"""


class Solution:
    def maxOperations(self, s: str) -> int:
        cnt1 = ans = 0  # cnt1 统计 1 的个数
        for i, c in enumerate(s):
            if c == "1":
                cnt1 += 1
            elif i and s[i - 1] == "1":  # 右边是 1 的 0 的位置
                ans += cnt1
        return ans


s = Solution()
examples = [
    (dict(s="1001101"), 4),
    (dict(s="00111"), 0),
]
for e, a in examples:
    print(a, e)
    print(s.maxOperations(**e))
