# 第 400 场周赛 第 1 题
# 题目：100307. 候诊室中的最少椅子数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-400/problems/minimum-number-of-chairs-in-a-waiting-room/
# 题库：https://leetcode.cn/problems/minimum-number-of-chairs-in-a-waiting-room


class Solution:
    def minimumChairs(self, s: str) -> int:
        a = ans = 0
        for c in s:
            a += 1 if c == "E" else -1
            ans = max(ans, a)
        return ans


s = Solution()
examples = [
    (dict(s="EEEEEEE"), 7),
    (dict(s="ELELEEL"), 2),
    (dict(s="ELEELEELLL"), 3),
]
for e, a in examples:
    print(a, e)
    print(s.minimumChairs(**e))
