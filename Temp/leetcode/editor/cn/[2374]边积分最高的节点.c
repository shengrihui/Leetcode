// 2374 边积分最高的节点
// https://leetcode.cn/problems/node-with-highest-edge-score/


//leetcode submit region begin(Prohibit modification and deletion)
int edgeScore(int* edges, int edgesSize) {
    long long* cnt = (long long*)malloc(sizeof(long long) * edgesSize);
    for (int i = 0; i < edgesSize; i++)
        cnt[i] = 0;
    for (int i = 0; i < edgesSize; i++) {
        cnt[edges[i]] += i;
    }
    int ans = 0;
    long long mx = 0;
    for (int i = 0; i < edgesSize; i++) {
        if (cnt[i] > mx) {
            mx = cnt[i];
            ans = i;
        }
    }
    free(cnt);
    return ans;
}

/*
int edgeScore(int* edges, int edgesSize) {
    int ans = 0;
    long long* score = calloc(edgesSize, sizeof(long long));
    for (int i = 0; i < edgesSize; i++) {
        int to = edges[i];
        score[to] += i;
        if (score[to] > score[ans] || score[to] == score[ans] && to < ans) {
            ans = to;
        }
    }
    free(score);
    return ans;
}
*/
//leetcode submit region end(Prohibit modification and deletion)
