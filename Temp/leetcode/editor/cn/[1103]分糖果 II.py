# 1103 分糖果 II
# https://leetcode.cn/problems/distribute-candies-to-people/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        left, right = 1, candies
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= candies:
                left = mid + 1
            else:
                right = mid - 1
        p, r = divmod(right, num_people)
        ans = [0] * num_people
        for i in range(num_people):
            if i < r:
                ans[i] = p * (p + 1) // 2 * num_people + (p + 1) * (i + 1)
            else:
                ans[i] = (p - 1) * p // 2 * num_people + p * (i + 1)
        ans[r] += candies - right * (right + 1) // 2
        return ans
# leetcode submit region end(Prohibit modification and deletion)
