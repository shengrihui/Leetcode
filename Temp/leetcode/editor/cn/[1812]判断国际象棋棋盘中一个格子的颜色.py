# 1812 判断国际象棋棋盘中一个格子的颜色
# https://leetcode.cn/problems/determine-color-of-a-chessboard-square/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        d = {c: i for i, c in enumerate("abcdefgh", 1)}
        i, j = d[coordinates[0]], int(coordinates[1])
        return (i - j) % 2 == 1


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) - ord('a') + 1 + int(coordinates[1])) % 2 == 1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/determine-color-of-a-chessboard-square/solutions/2009904/pan-duan-guo-ji-xiang-qi-qi-pan-zhong-yi-8dv4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
