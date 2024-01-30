from collections import defaultdict

# 题目：# 8040. 生成特殊数字的最少操作
# 题目链接：https://leetcode.cn/problems/minimum-operations-to-make-a-special-number/description/
# 第 361 场周赛
# Q2
# 1588

# 方法一
"""
class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        # num 里既没有 5 也没有 0，那它一定不能变成 25 的倍数
        if "5" not in num and "0" not in num:
            return len(num)
        if n < 3:  # 一位数和两位数
            if num[-1] == "0" and num != "50":  # x0 和 0
                return n - 1
            if num not in ["25", "50", "75"]:  # 除了这几个全删除
                return n
            else:
                return 0
        d = defaultdict(list)
        for i, c in enumerate(num):
            if c in "2507":
                d[c].append(i)

        ans = n - ("0" in num)

        def f(a: str, b: str) -> None:
            nonlocal ans
            for i in d[a]:
                for j in d[b]:
                    if i < j:
                        ans = min(ans, n - i - 2)

        # 让最后两位是 x
        for x in ["25", "50", "75", "00"]:
            f(x[0], x[1])

        return ans
"""


class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n - ("0" in num)

        def f(tail: str) -> int:
            i = num.rfind(tail[1])
            if i < 0: return ans
            i = num.rfind(tail[0], 0, i)
            if i < 0: return ans
            return n - i - 2

        return min(f(t) for t in ["00", "25", "50", "75"])


s = Solution()
examples = [
    (dict(num="2245047"), 2),
    (dict(num="2908305"), 3),
    (dict(num="10"), 1),
    (dict(num="50"), 0),
    (dict(num="75"), 0),
    (dict(num="175"), 0),
    (dict(num="820366"), 5),
    (dict(num="53478"), 5),
]
for e, a in examples:
    print(a, e)
    print(s.minimumOperations(**e))
