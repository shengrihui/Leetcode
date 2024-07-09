# 2673 使二叉树所有路径值相等的最小代价
# https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def dfs_mx(i: int, s: int) -> None:
            if i * 2 + 1 > n:
                nonlocal mx
                mx = max(mx, s)
                return
            dfs_mx(i * 2, s + cost[i * 2 - 1])
            dfs_mx(i * 2 + 1, s + cost[i * 2])

        def dfs(i: int, s: int) -> int:
            # s: 到 i 的路径和
            nonlocal ans, mx
            if i * 2 + 1 > n:  # 叶子节点
                return mx - s
            l = dfs(i * 2, s + cost[i * 2 - 1])
            r = dfs(i * 2 + 1, s + cost[i * 2])
            ans += abs(l - r)  # 左/右子树，整个子树要操作的次数之差
            return min(l, r)  # 对于 i，操作 l和r 的较小值

        ans, mx = 0, 0
        dfs_mx(1, cost[0])
        t = dfs(1, cost[0])
        return ans + t

# class Solution:
#     def minIncrements(self, n: int, cost: List[int]) -> int:
#         ans = 0
#         for i in range(n - 2, 0, -2):
#             ans += abs(cost[i] - cost[i + 1])
#             # 叶节点 i 和 i+1 的双亲节点下标为 i/2（整数除法）
#             cost[i // 2] += max(cost[i], cost[i + 1])
#         return ans
#
# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/solutions/2656293/shi-er-cha-shu-suo-you-lu-jing-zhi-xiang-65hk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
