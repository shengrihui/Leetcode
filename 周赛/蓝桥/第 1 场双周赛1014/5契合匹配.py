# 题目：# 5契合匹配
# 题目链接：https://www.lanqiao.cn/problems/5132/learning/?contest_id=144
def build_partial_match_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            if j > 0:
                j = table[j - 1]
                i -= 1
            else:
                table[i] = 0
    return table


def kmp_search(text, pattern):
    partial_match_table = build_partial_match_table(pattern)
    i, j = 0, 0
    while i < len(text) and j < len(pattern):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = partial_match_table[j - 1]
            else:
                i += 1
    if j == len(pattern):
        return i - j
    else:
        return -1


n = int(input())
A = input()
B = list(input())
for i, b in enumerate(B):
    if b.isupper():
        B[i] = chr(32 + ord(b))
    else:
        B[i] = chr(ord(b) - 32)
B = "".join(B)
AA = A + A
i = kmp_search(AA, B)
if i == -1:
    print("No")
else:
    print("Yes")
    print(min(i, n - i))

"""
5
AbbCd
BcDaB
"""
