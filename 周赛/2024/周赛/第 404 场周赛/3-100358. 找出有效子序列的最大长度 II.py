# 第 404 场周赛 第 3 题
# 题目：100358. 找出有效子序列的最大长度 II
# 题目链接：
# 竞赛：https://leetcode.cn/contest/weekly-contest-404/problems/find-the-maximum-length-of-valid-subsequence-ii/
# 题库：https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-ii

from typing import List


# 子序列的奇数位 % k 都相等，偶数位 % k 都相等
# 都 % k 后子序列就形如 xyxyxyxy
# 知道前两或后两个就知道整个子序列
# f[x][y] 最后两个是 xy 的子序列的数量
# f[x][y] = f[y][x] + 1
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        f = [[0] * k for _ in range(k)]
        for x in nums:
            x %= k
            for y in range(k):
                f[y][x] = f[x][y] + 1
        return max(map(max, f))


# 空间优化
# 知道了 m=(y+x)%k 和 x 就可以知道这个子序列了
# 遍历 m
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = [x % k for x in nums]
        for m in range(k):
            f = [0] * k
            for x in nums:
                f[x] = f[m - x] + 1  # (m - x) $ k python就不用了
            ans = max(ans, max(f))
        return ans


s = Solution()
examples = [
    (dict(nums=[1, 1, 7, 3, 2], k=2), 4),
    (dict(nums=[2, 1, 4, 1, 3], k=3), 3),
    (dict(nums=[1, 2, 3, 4, 5], k=2), 5),
    (dict(nums=[1, 4, 2, 3, 1, 4], k=3), 4),
]
for e, a in examples:
    print(a, e)
    print(s.maximumLength(**e))
