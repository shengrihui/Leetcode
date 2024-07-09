# 365 水壶问题
# https://leetcode.cn/problems/water-and-jug-problem/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canMeasureWater(self, a: int, b: int, target: int) -> bool:
        if a + b < target: return False
        q = deque([(a, 0), (0, b)])
        vis = {(a, 0), (0, b)}
        while q:
            aa, bb = q.popleft()
            for na, nb in [(0, bb), (max(0, aa - (b - bb)), min(b, aa + bb)), (a, bb),
                           (min(a, aa + bb), max(0, bb - (a - aa))), (aa, 0), (aa, b)]:
                # print(na, nb)
                if na == target or nb == target or na + nb == target:
                    return True
                if not (na, nb) in vis:
                    vis.add((na, nb))
                    q.append((na, nb))
        return False

# class Solution:
#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         if x + y < z:
#             return False
#         if x == 0 or y == 0:
#             return z == 0 or x + y == z
#         return z % math.gcd(x, y) == 0
#
# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/water-and-jug-problem/solutions/161010/shui-hu-wen-ti-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# leetcode submit region end(Prohibit modification and deletion)
