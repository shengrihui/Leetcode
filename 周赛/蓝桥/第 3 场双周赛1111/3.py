# 题目：# 3
# 题目链接：https://www.lanqiao.cn/problems/6278/learning/?contest_id=146

s = "ShallowDream"
j = "Joker"
order = "3456789XJQKA2MF"
d = {c: i for i, c in enumerate(order)}
T = int(input())
for _ in range(T):
    s1, s2 = input().split()
    s1 = "".join(sorted(list(set(s1)), key=lambda c: d[c]))
    s2 = "".join(sorted(list(set(s2)), key=lambda c: d[c]))
    print(s1, s2)
    if s1 == "MF" or len(s1) == 1:
        print(s)
        continue
    if s2 == "MF":
        print(j)
        continue
    # 第一个人一定有两张牌
    if d[s1[1]] < d[s2[-1]]:
        print(j)
    else:
        print(s)
