// 997 找到小镇的法官
// https://leetcode.cn/problems/find-the-town-judge/


//leetcode submit region begin(Prohibit modification and deletion)
int findJudge(int n, int** trust, int trustSize, int* trustColSize) {
    int* inDeg = (int*)malloc(sizeof(int) * (n + 1));
    memset(inDeg, 0, sizeof(int) * (n + 1));
    int* outDeg = (int*)malloc(sizeof(int) * (n + 1));
    memset(outDeg, 0, sizeof(int) * (n + 1));
    for (int i = 0; i < trustSize; i++) {
        int a = trust[i][0], b = trust[i][1];
        inDeg[b]++;
        outDeg[a]++;
    }
    for (int i = 1; i <= n; i++) {
        if (inDeg[i] == n - 1 && outDeg[i] == 0)
            return i;
    }
    free(inDeg);
    free(outDeg);
    return -1;
}
//leetcode submit region end(Prohibit modification and deletion)
