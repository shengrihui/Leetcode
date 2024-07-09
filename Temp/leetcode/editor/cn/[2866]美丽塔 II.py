# 2866 美丽塔 II
# https://leetcode.cn/problems/beautiful-towers-ii/


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        pre = [0] * n  # pre[i] i 作为山顶它前面（包括 i ）高度和
        st = [-1]  # 存下标
        for i, h in enumerate(maxHeights):
            while len(st) > 1 and maxHeights[st[-1]] >= h:
                st.pop()
            # st[-1]+1 到 i 都是 h
            # st = [] 的写法
            # pre[i] = (pre[st[-1]] if st else 0) + h * (i - st[-1] if st else i+1)
            # 当 i=n-1 的时候，st 现在只有 [-1] ,res[st[-1]]=pre[-1]=0，所以 st 可以加一个哨兵 -1
            pre[i] = pre[st[-1]] + h * (i - st[-1])
            st.append(i)

        ans = 0
        st = [n]  # 存下标
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            h = maxHeights[i]
            while len(st) > 1 and maxHeights[st[-1]] >= h:
                st.pop()
            # i 到 st[-1]-1 都是 h
            suf[i] = suf[st[-1]] + h * (st[-1] - i)
            st.append(i)
            ans = max(ans, suf[i] + pre[i] - h)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
