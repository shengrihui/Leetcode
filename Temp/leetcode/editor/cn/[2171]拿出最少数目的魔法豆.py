# 2171 拿出最少数目的魔法豆
# https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        ans = total = sum(beans)
        for i, x in enumerate(beans):
            ans = min(ans, total - x * (n - i))
        return ans
    # def minimumRemoval(self, beans: List[int]) -> int:
    #     beans.sort()
    #     n = len(beans)
    #     pre_sum = [0] * (n + 1)
    #     for i, x in enumerate(beans, 1):
    #         pre_sum[i] = pre_sum[i - 1] + x
    #     ans = pre_sum[-1]  # 全部拿走
    #     for i in range(1, n + 1):
    #         # 前 i 小全部拿走，后面都变成 beans[i-1]
    #         t = pre_sum[i - 1] + (pre_sum[-1] - pre_sum[i]) - beans[i - 1] * (n - i)
    #         ans = min(ans, t)
    #     return ans
# leetcode submit region end(Prohibit modification and deletion)
