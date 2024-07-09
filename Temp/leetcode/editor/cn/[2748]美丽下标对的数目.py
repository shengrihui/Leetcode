# 2748 美丽下标对的数目
# https://leetcode.cn/problems/number-of-beautiful-pairs/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        # cnt[i] 统计 x 之前的数中，第一位数是 i 的有几个
        cnt = [0] * 10
        for x in nums:
            for y, c in enumerate(cnt):
                if c and gcd(y, x % 10) == 1:
                    ans += c
            while x >= 10:
                x //= 10
            cnt[x] += 1
        return ans


"""
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a, b = int(str(nums[i])[0]), int(str(nums[j])[-1])
                ans += gcd(a, b) == 1
        return ans
"""
# leetcode submit region end(Prohibit modification and deletion)
