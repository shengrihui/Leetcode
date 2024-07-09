# 375 猜数字大小 II
# https://leetcode.cn/problems/guess-number-higher-or-lower-ii/


# leetcode submit region begin(Prohibit modification and deletion)

@cache
def dfs(i: int, j: int) -> int:
    if i >= j:
        return 0
    if i + 1 == j:
        return i
    res = 20000
    for k in range(i, j + 1):
        res = min(res, k + max(dfs(i, k - 1), dfs(k + 1, j)))
    return res


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return dfs(1, n)
# leetcode submit region end(Prohibit modification and deletion)
