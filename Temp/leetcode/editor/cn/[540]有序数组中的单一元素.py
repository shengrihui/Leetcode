# 540 有序数组中的单一元素
# https://leetcode.cn/problems/single-element-in-a-sorted-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/single-element-in-a-sorted-array/solutions/1252764/you-xu-shu-zu-zhong-de-dan-yi-yuan-su-by-y8gh
# 单一元素的下标是 x
# 在 x 的左边，若 nums[y] == nums[y + 1]，那 y 是偶数
# 在 x 的右边，若 nums[z] == nums[z + 1]，那 z 是奇数
# x 是 nums[i] == nums[i + 1] i 的奇偶分界
# 二分
# 若 mid 是偶数，比较 nums[mid] == nums[mid + 1]
#   相等，移动左端点，不相等，移动右端点
# 若 mid 是奇数，比较 nums[mid] == nums[mid + 1]
#   相等，移动右端点，不相等，移动左端点
#   或者，比较 nums[mid] == nums[mid - 1]
#   这样，比较的结果和移动断点的情况和上面一样
# 异或
# mid 奇数，mid ^ 1 = mid - 1
# mid 偶数，mid ^ 1 = mid + 1
# 无需判断奇偶了。
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid - 1
        # high 的左边 [0, low] 都满足 nums[i] == nums[i+1] i 是偶数，所以 low 是答案
        return nums[low]


# 根据 [i,m] 的数量判断
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i != j:
            m = (i + j) // 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            if (m - i) % 2 == 1:
                if nums[m] == nums[m - 1]:
                    i = m + 1
                elif nums[m] == nums[m + 1]:
                    j = m - 1
            else:
                if nums[m] == nums[m - 1]:
                    j = m
                elif nums[m] == nums[m + 1]:
                    i = m
        return nums[i]
# leetcode submit region end(Prohibit modification and deletion)
