# 2808 使循环数组所有元素相等的最少秒数
# https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = ans = len(nums)
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        for pos_list in d.values():
            mx = pos_list[0] + n - pos_list[-1] - 1  # 相邻两个相同数之间最大的距离
            for x, y in pairwise(pos_list):
                mx = max(mx, y - x - 1)
            ans = min(ans, (mx + 1) // 2)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
