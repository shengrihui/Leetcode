# 503 下一个更大元素 II
# https://leetcode.cn/problems/next-greater-element-ii/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []  # 单调递减栈
        ans = [-1] * n
        for i in range(n * 2):
            while st and nums[st[-1]] < nums[i % n]:  # nums[i%n] 比 nums[st[-1]] 大
                ans[st.pop()] = nums[i % n]
            st.append(i % n)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
