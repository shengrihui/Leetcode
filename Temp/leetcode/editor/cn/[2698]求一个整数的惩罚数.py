# 2698 求一个整数的惩罚数


# leetcode submit region begin(Prohibit modification and deletion)
def dfs(j: int, s: int) -> bool:
    global square_str
    if j < 0:
        return False
    for l in range(j, -1, -1):
        p = int(square_str[l:j + 1])
        if p > s:
            return False
        elif p == s:
            return l == 0
        else:
            if dfs(l - 1, s - p):
                return True


punishment_i = []
for i in range(1, 1001):
    square_int = i * i
    square_str = str(square_int)
    if dfs(len(square_str) - 1, i):
        punishment_i.append(i)


# print(punishment_i)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(i * i for i in punishment_i if i <= n)
# leetcode submit region end(Prohibit modification and deletion)
