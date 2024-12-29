T = int(input())

for _ in range(T):
    n, m = list(map(int, input().split()))
    a = []
    ones = 0
    for j in range(n):
        t = list(input())
        a.append(t)
        ones += t[1:-1].count("1")
    if n == 1 or m == 1:
        if a[0][0] == "0" or a[0][-1] == "0" or a[-1][0] == "0" or a[-1][-1] == "0":
            print(-1)
        else:
            print(1)
        continue
    # 下面不止一行/列
    # 对角有，1 次
    if a[-1][-1] == a[0][0] == "1" or a[0][-1] == a[-1][0] == "1":
        print(1)
        continue
    aa = list(zip(*a))
    r1, r2 = a[0].count("1") > 0, a[-1].count("1") > 0
    c1, c2 = aa[0].count("1") > 0, aa[-1].count("1") > 0
    one = r1 + r2 + c1 + c2
    if one <= 3:
        print(-1)
        continue
    corner = (a[-1][-1] == "1") + (a[0][0] == "1") + (a[0][-1] == "1") + (a[-1][0] == "1")
    if ones > 0 and corner > 0:
        print(2)
        continue
    if a[0][-1] == "1" and a[0][0] == "1" and r2 > 0 or \
            a[0][0] == "1" and a[-1][0] == "1" and c2 > 0 or \
            a[0][-1] == "1" and a[-1][-1] == "1" and c1 > 0 or \
            a[-1][-1] == "1" and a[-1][0] == "1" and r1 > 0:
        print(2)
        continue
    print(3)

"""
4
2 2
01
00
3 3
010
111
011
3 4
0000
1111
0110

1
3 4
0000
0001
1001

1
3 1
1
0
1

-1
1
2
"""
