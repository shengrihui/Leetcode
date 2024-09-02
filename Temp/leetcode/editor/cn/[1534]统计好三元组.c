// 1534 统计好三元组
// https://leetcode.cn/problems/count-good-triplets/


//leetcode submit region begin(Prohibit modification and deletion)


int countGoodTriplets(int* arr, int arrSize, int a, int b, int c) {
    int ans = 0;
    for (int i = 0; i < arrSize - 2; i++) {
        for (int j = i + 1; j < arrSize - 1; j++) {
            if (abs(arr[i] - arr[j]) > a)
                continue;
            for (int k = j + 1; k < arrSize; k++)
                ans += abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c;
        }
    }
    return ans;
}
//leetcode submit region end(Prohibit modification and deletion)
