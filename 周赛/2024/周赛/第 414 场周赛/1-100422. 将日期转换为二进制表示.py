# 第 414 场周赛 第 1 题
# 题目：100422. 将日期转换为二进制表示
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-414/problems/convert-date-to-binary/
# 题库：https://leetcode.cn/problems/convert-date-to-binary


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # s = date.split('-')
        # ans = []
        # for t in s:
        #     ans.append(bin(int(t))[2:])
        # return "-".join(ans)
        return "-".join([str(bin(int(s))[2:]) for s in date.split("-")])


s = Solution()
examples = [
    (dict(date="2080-02-29"), "100000100000-10-11101"),
    (dict(date="1900-01-01"), "11101101100-1-1"),
]
for e, a in examples:
    print(a, e)
    print(s.convertDateToBinary(**e))
