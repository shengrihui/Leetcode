# 2735 收集巧克力
# https://leetcode.cn/problems/collecting-chocolates/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = nums.copy()
        ans = sum(s)
        # 不能在 i 循环的时候加 x*k
        # 因为不同的类型的可能会在同一次加 x*k ，会重复
        for k in range(1, n):  # 操作次数
            for i in range(n):  # 类型
                s[i] = min(s[i], nums[(i + k) % n])
            ans = min(ans, sum(s) + k * x)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

"""
[15,150,56,69,214,203]
42

"""
