# 2103 环和杆


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPoints(self, rings: str) -> int:
        d = {"R": 1, "G": 2, "B": 4}
        s = [0] * 10
        for i in range(0, len(rings), 2):
            c, r = rings[i], rings[i + 1]
            s[int(r)] |= d[c]
        return sum(i == 7 for i in s)
# leetcode submit region end(Prohibit modification and deletion)
