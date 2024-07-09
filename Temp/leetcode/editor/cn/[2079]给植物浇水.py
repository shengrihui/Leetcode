# 2079 给植物浇水
# https://leetcode.cn/problems/watering-plants/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        rest = capacity
        for i, x in enumerate(plants):
            if rest < x:
                rest = capacity
                ans += i * 2
            ans += 1
            rest -= x
        return ans
# leetcode submit region end(Prohibit modification and deletion)
