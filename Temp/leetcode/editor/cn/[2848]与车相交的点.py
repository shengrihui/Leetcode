# 2848 与车相交的点
# https://leetcode.cn/problems/points-that-intersect-with-cars/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        diff = [0] * 102
        max_end = max(end for _, end in nums)
        diff = [0] * (max_end + 2)
        for start, end in nums:
            # 区间 [start,end] 的值都加1
            # 差分数组修改 start和end+1
            # 对应差分数组的前缀和数组中大于0的位置就是有车的位置
            diff[start] += 1
            diff[end + 1] -= 1
        # ans = 0
        # pre = [0] * (max_end + 2)
        # for i, x in enumerate(diff[1:]):
        #     pre[i] = pre[i - 1] + diff[i]
        #     ans += pre[i] > 0
        # print(diff)
        # print(pre)
        # return ans
        return sum(x > 0 for x in accumulate(diff))
# leetcode submit region end(Prohibit modification and deletion)
