# 2660 保龄球游戏的获胜者
# https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(player):
            res = 0
            for i, x in enumerate(player):
                if i > 0 and player[i - 1] == 10 or i > 1 and player[i - 2] == 10:
                    res += 2 * x
                else:
                    res += x
            return res

        p1, p2 = score(player1), score(player2)
        if p1 == p2:
            return 0
        if p1 < p2:
            return 2
        return 1

# class Solution:
#     def isWinner(self, player1: List[int], player2: List[int]) -> int:
#         p1, p2 = player1[0], player2[0]
#         n = len(player1)
#         if n >= 2:
#             p1 += player1[1] * 2 if player2[0] == 10 else player1[0]
#             p2 += player2[1] * 2 if player1[0] == 10 else player2[0]
#             p1 += sum(
#                 2 * player1[i] if player1[i - 1] == 10 or player1[i - 2] == 10 else player1[i] for i in range(2, n))
#             p2 += sum(
#                 2 * player2[i] if player2[i - 1] == 10 or player2[i - 2] == 10 else player2[i] for i in range(2, n))
#         if p1 == p2:
#             return 0
#         if p1 < p2:
#             return 2
#         return 1
# leetcode submit region end(Prohibit modification and deletion)
