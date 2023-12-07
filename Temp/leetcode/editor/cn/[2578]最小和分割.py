# 2578 最小和分割


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitNum(self, num: int) -> int:
        nums_list = list(str(num))
        nums_list.sort()
        nums1 = int("".join(nums_list[::2]))
        nums2 = int("".join(nums_list[1::2]))
        return nums1 + nums2
# leetcode submit region end(Prohibit modification and deletion)
