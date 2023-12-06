# 2569 更新数组后处理求和查询
from typing import *
from collections import *
from itertools import *
from functools import *
from math import *
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # 操作1：将 nums1 的 [l,r] 的 0/1 翻转
        # 操作3：输出 nums2 的和
        # 所以 nums2 每一个值是多少并不重要，关注 nums2 的和（用一个变量记录）
        # 操作2的作用就是将 nums1 的和的 p 倍加到 nums2 的和上去
        # cnt1[o]：编号为 o 的节点的区间1的个数
        # flip[o]：编号为 o 的节点的区间里是否进行了 0/1 翻转
        n = len(nums1)
        cnt1 = [0] * (4 * n)
        flip = [False] * (4 * n)

        def maintain(o: int) -> int:
            # 计算节点编号为 o 所代表的区间里有多少1
            # 也就是节点 o 的左右儿子的 cnt1 和
            # 在 build 和 update 的时候用
            cnt1[o] = cnt1[o * 2] + cnt1[o * 2 + 1]

        def build(o: int, l: int, r: int) -> None:
            # o：当前节点编号；l，r:当前节点的区间范围
            if l == r:  # 当区间长度只有1的时候，停止递归
                # 这道题是要维护区间内有多少个1
                # 所以当 l == r，cnt1[o] 就是对应 nums1 的值
                # l-1 是因为在线段树里，区间下标从1开始
                cnt1[o] = nums1[l - 1]
                return
            m = (l + r) // 2
            build(o * 2, l, m)  # 左儿子
            build(o * 2 + 1, m + 1, r)  # 右儿子
            maintain(o)

        def do(o: int, l: int, r: int) -> None:
            # 对编号为 o 的节点进行更新操作
            # 在 update 里用
            # 在这道题里
            # 更新操作是操作1干的翻转 0/1
            # 一个区间的 0/1 反转了，cnt1[0] 变为 区间长度 - 原来有多少个1
            cnt1[o] = r - l + 1 - cnt1[o]
            # flip[o] 取反即可
            flip[o] = not flip[o]

        def update(o: int, l: int, r: int, L: int, R: int) -> None:
            # o：当前节点编号；
            # l，r:当前节点的区间范围
            # L,R：要更新的区间的范围
            if l >= L and r <= R:
                # 当前节点完全在要更新的区间范围里(区间内所有的点都要进行更新)
                # 那就对这个节点进行操作之后就 return，不在继续递归下去
                do(o, l, r)
                return
            # 没有进入上面这个 if-return，说明
            # 这个节点的区间 [l,r] 包含了一些这次更新范围外的区间
            # 还要递归下去
            m = (l + r) // 2

            # 先将更新标记传递下去，并将 o 的标记取消掉
            # cnt1[o] 的修改在最后面，左右儿子递归完了再维护
            if flip[o]:
                do(o * 2, l, m)
                do(o * 2 + 1, m + 1, r)
                flip[o] = False

            if not m < L:  # l<m<L ：左儿子没有要更新的区间，不用继续递归下去
                update(o * 2, l, m, L, R)  # 左儿子
            if not R < m + 1:  # R<m+1<r ：右儿子没有要更新的区间，不用继续递归下去
                update(o * 2 + 1, m + 1, r, L, R)  # 右儿子
            maintain(o)

        build(1, 1, n)  # 初始化，第一个节点的编号为1，区间范围为[1,n]
        ans, s = [], sum(nums2)
        for op, l, r in queries:
            if op == 1:
                update(1, 1, n, l + 1, r + 1)  # +1因为下标从1开始
            elif op == 2:  # [2,p,0] l==p
                s += l * cnt1[1]  # cnt[1]代表nums1里有毒少个1
            elif op == 3:
                ans.append(s)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


# 给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作： 
# 
#  
#  操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 并且所有 1 反转
# 成 0 。l 和 r 下标都从 0 开始。 
#  操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] +
#  nums1[i] * p 。 
#  操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。 
#  
# 
#  请你返回一个 数组，包含 所有第三种操作类型 的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
# 输出：[3]
# 解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。
# 
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
# 输出：[5]
# 解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length,nums2.length <= 10⁵ 
#  nums1.length = nums2.length 
#  1 <= queries.length <= 10⁵ 
#  queries[i].length = 3 
#  0 <= l <= r <= nums1.length - 1 
#  0 <= p <= 10⁶ 
#  0 <= nums1[i] <= 1 
#  0 <= nums2[i] <= 10⁹ 
#  
# 
#  Related Topics 线段树 数组 👍 99 👎 0
