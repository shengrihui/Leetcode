# import requests
# a={"operationName": "progressSubmissions",
#  "variables": {"offset": 0, "limit": 10, "questionSlug": "construct-product-matrix"},
#  "query": "query progressSubmissions($offset: Int, $limit: Int, $lastKey: String, $questionSlug: String) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      timestamp\n      url\n      lang\n      runtime\n      __typename\n    }\n    __typename\n  }\n}\n"}
#
# res=requests.post("https://leetcode.cn/graphql/",data=a)
# print(res)
# print(res.text)

# 函数内修改列表的值，会影响外面
# def f(a):
#     print(a)
#     a[0] = 666
#     print(a)
#
#
# a = [1, 2, 3]
# f(a)
# print(a)


# from sortedcontainers import SortedList
#
#
# # sl = SortedList(key=lambda x: x[1])
# # sl.add([1, 100])
# # sl.add([3, 2])
# # sl.add([2, 200])
# class Node:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __lt__(self, other):
#         return self.a < other.a
#
#     def __gt__(self, other):
#         return self.b > other.b
#
#
# a = Node(1, 150)
# b = Node(2, 200)
# c = Node(3, 100)
# d = Node(4, 120)
# lst = [Node(1, 150),
#        Node(2, 200),
#        Node(3, 100),
#        Node(0, 190),
#        Node(4, 120)]
# sl = SortedList(lst)
# for n in sl:
#     print(n.a, n.b)
# mx = max(sl)
# mn = min(sl)
# print()
# print("mx b", mx.a, mx.b)
# print("mn a", mn.a, mn.b)

# class Node:
#     def __init__(self):
#         pass
#     def __len__(self):
#         return 0
# n=Node()
# print(len(n))


def f(x, p):
    if x == 5:
        return
    p[x] += 1
    print(x, p)
    f(x + 1, p)
    print(x, p)


a = 0
lst = [0] * 100
f(1,lst)
