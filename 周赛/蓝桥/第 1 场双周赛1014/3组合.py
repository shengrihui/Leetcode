# 题目：# 3组合
# 题目链接：


def check(m):
    arr = [h[0]]
    for x in h[1:]:
        if x - arr[-1] > m:
            arr.append(x)
    return len(arr) > k


n, k = map(int, input().split())
h = sorted(set(map(int, input().split())))
l, r = 0, h[-1] - h[0]
while l <= r:
    mid = (l + r) // 2
    if check(mid):  # mid能分的组比k多，小了
        l = mid + 1
    else:  # 刚好能分k组，或者不够k组，还不够小
        r = mid - 1
print(l)

"""
5 3
8 4 3 6 9
"""
