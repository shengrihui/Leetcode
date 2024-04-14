# 第 393 场周赛 第 1 题
# 题目：100256. 替换字符可以得到的最晚时间
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-393/problems/latest-time-you-can-obtain-after-replacing-characters/
# 题库：https://leetcode.cn/problems/latest-time-you-can-obtain-after-replacing-characters


class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[0] == "?":
            s[0] = ("1" if s[1] == "?" or s[1] != "?" and int(s[1]) <= 1 else "0")
        if s[1] == "?":
            s[1] = ("1" if s[0] == "1" else "9")
        if s[3] == "?": s[3] = "5"
        if s[4] == "?": s[4] = "9"
        return "".join(s)


class Solution:
    def findLatestTime(self, s: str) -> str:
        for h in range(11, -1, -1):
            for m in range(59, -1, -1):
                t = f"{h:02d}:{m:02d}"
                if all(x == y for x, y in zip(s, t) if x != "?"):
                    return t


s = Solution()
examples = [
    (dict(s="??:1?"), "11:19"),
    (dict(s="?3:12"), "03:12"),
    (dict(s="1?:?4"), "11:54"),
    (dict(s="0?:5?"), "09:59"),
]
for e, a in examples:
    print(a, e)
    print(s.findLatestTime(**e))
