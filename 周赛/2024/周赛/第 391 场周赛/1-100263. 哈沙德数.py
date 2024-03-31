# 第 391 场周赛 第 1 题
# 题目：100263. 哈沙德数
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-391/problems/harshad-number/
# 题库：https://leetcode.cn/problems/harshad-number


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(map(int, str(x)))
        if x % s == 0:
            return s
        return -1


s = Solution()
examples = [
    (dict(x=18), 9),
]
for e, a in examples:
    print(a, e)
    print(s.sumOfTheDigitsOfHarshadNumber(**e))
