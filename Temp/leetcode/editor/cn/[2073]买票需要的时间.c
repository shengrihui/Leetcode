// 2073 买票需要的时间
// https://leetcode.cn/problems/time-needed-to-buy-tickets/

//leetcode submit region begin(Prohibit modification and deletion)
#define min(a, b) (a) < (b) ? (a) : (b)
int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    int tk = tickets[k];
    int ans = 0;
    for (int i = 0; i < ticketsSize; i++) {
        /*
        if (i <= k) // 在 k 前面的人最多买 tk 张漂
            ans += min(tk, tickets[i]);
        else
            ans += min(tk - 1, tickets[i]);
            */
        ans += min(tk - (i > k), tickets[i]);
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
