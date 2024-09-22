// 1014 最佳观光组合
// https://leetcode.cn/problems/best-sightseeing-pair/


//leetcode submit region begin(Prohibit modification and deletion)
int maxScoreSightseeingPair(int* values, int valuesSize) {
    int ans = 0, mx = 0;
    for (int i = 0; i < valuesSize; i++) {
        int v = values[i];
        if (v - i + mx > ans)
            ans = v - i + mx;
        if (v + i > mx)
            mx = v + i;
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
