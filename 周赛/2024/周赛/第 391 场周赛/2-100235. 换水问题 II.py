# 第 391 场周赛 第 2 题
# 题目：100235. 换水问题 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-391/problems/water-bottles-ii/
# 题库：https://leetcode.cn/problems/water-bottles-ii


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        numBottles = 0
        while empty >= numExchange:
            empty -= numExchange
            numExchange += 1
            ans += 1
            empty += 1
        return ans


s = Solution()
examples = [
    (dict(numBottles=10, numExchange=3), 13)
]
for e, a in examples:
    print(a, e)
    print(s.maxBottlesDrunk(**e))
