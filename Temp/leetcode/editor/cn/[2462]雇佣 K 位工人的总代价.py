# 2462 雇佣 K 位工人的总代价
# https://leetcode.cn/problems/total-cost-to-hire-k-workers/

# leetcode submit region begin(Prohibit modification and deletion)

# 一个堆
"""
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        # 所有都入堆了
        if candidates * 2 + k > n:
            costs.sort()
            return sum(costs[:k])
        q = [(costs[i], i) for i in range(candidates)]
        for j in range(n - 1, max(n - candidates - 1, candidates - 1), -1):
            q.append((costs[j], j))
        heapq.heapify(q)
        i, j = candidates, n - 1 - candidates
        total = 0
        for ii in range(k):
            c, idx = heapq.heappop(q)
            total += c
            if i <= j:
                if idx < i:
                    heapq.heappush(q, (costs[i], i))
                    i += 1
                elif idx > j:
                    heapq.heappush(q, (costs[j], j))
                    j -= 1
                # print(q)
        return total
"""


# 灵神两个堆
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 + k > n:
            # 也可以 sum(nsmallest(k, costs))，但效率不如直接排序
            costs.sort()
            return sum(costs[:k])

        pre = costs[:candidates]
        suf = costs[-candidates:]
        heapify(pre)
        heapify(suf)

        ans = 0
        i = candidates
        j = n - 1 - candidates
        for _ in range(k):
            if pre[0] <= suf[0]:
                ans += heapreplace(pre, costs[i])
                i += 1
            else:
                ans += heapreplace(suf, costs[j])
                j -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
"""
[17,12,10,2,7,2,11,20,8]
3
4
[1,2,4,1]
3
3
[18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75]
3
23
[17,12,10,2,7,2,11,20,8]
3
4
[60,87,94,42,12,60]
			5
			4

"""
