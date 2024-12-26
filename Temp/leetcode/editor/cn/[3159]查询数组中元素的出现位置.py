# 3159 查询数组中元素的出现位置
# https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indies = []
        for i, a in enumerate(nums):
            if a == x:
                indies.append(i)
        ans = []
        for q in queries:
            if q > len(indies):
                ans.append(-1)
            else:
                ans.append(indies[q - 1])
        return ans


"""
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        pos = [i for i, num in enumerate(nums) if num == x]
        return [-1 if q > len(pos) else pos[q - 1] for q in queries]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-occurrences-of-an-element-in-an-array/solutions/2790398/ji-lu-suo-you-deng-yu-x-de-yuan-su-xia-b-ku53/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
# leetcode submit region end(Prohibit modification and deletion)
