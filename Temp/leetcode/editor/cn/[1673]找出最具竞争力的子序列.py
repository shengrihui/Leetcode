# 1673 找出最具竞争力的子序列
# https://leetcode.cn/problems/find-the-most-competitive-subsequence/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        for idx, x in enumerate(nums):
            while st and st[-1] > x and len(st) + len(nums) - idx > k:
                st.pop()
            if len(st) < k:
                st.append(x)
        return st
# leetcode submit region end(Prohibit modification and deletion)
