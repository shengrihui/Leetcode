// 1486 数组异或操作
// https://leetcode.cn/problems/xor-operation-in-an-array/


//leetcode submit region begin(Prohibit modification and deletion)
/*
int sumXOR(int n) {
    // 计算 0 到 n 的异或和
    switch (n % 4) {
    case 0:
        return n;
    case 1:
        return 1;
    case 2:
        return n + 1;
    default:
        return 0;
    }
}

int xorOperation(int n, int start) {
    int a = start / 2;
    int b = n & start & 1;
    return (sumXOR(a - 1) ^ sumXOR(a + n - 1)) * 2 + b;
}
*/

// https://leetcode.cn/problems/xor-operation-in-an-array/solutions/2793723/o1-gong-shi-tui-dao-pythonjavaccgojsrust-le23

int xorOperation(int n, int start) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        res ^= start + 2 * i;
    }
    return res;
}
//leetcode submit region end(Prohibit modification and deletion)
