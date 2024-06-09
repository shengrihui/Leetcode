# 第 401 场周赛 第 1 题
# 题目：100325. 找出 K 秒后拿着球的孩子
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-401/problems/find-the-child-who-has-the-ball-after-k-seconds/
# 题库：https://leetcode.cn/problems/find-the-child-who-has-the-ball-after-k-seconds


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # a, b = 0, 1
        # for _ in range(k):
        #     a += b
        #     if a == n - 1 or a == 0:
        #         b *= -1
        # return a
        q, r = divmod(k, n - 1)
        return n - 1 - r if q % 2 else r


s = Solution()
examples = [
    (dict(n=3, k=5), 1),
    (dict(n=5, k=6), 2),
    (dict(n=4, k=2), 2),
]
for e, a in examples:
    print(a, e)
    print(s.numberOfChild(**e))
