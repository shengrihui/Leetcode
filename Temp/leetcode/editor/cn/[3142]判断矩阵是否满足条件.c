// 3142 判断矩阵是否满足条件
// https://leetcode.cn/problems/check-if-grid-satisfies-conditions/

//leetcode submit region begin(Prohibit modification and deletion)
bool satisfiesConditions(int** grid, int gridSize, int* gridColSize) {
    for(int i = 0; i < gridSize; i++){
        for(int j = 0; j < gridColSize[i]; j++)
            if(i < gridSize - 1 && grid[i][j] != grid[i + 1][j] || j < gridColSize[i] - 1 && grid[i][j] == grid[i][j + 1])
                return false;
    }
    return true;
}
//leetcode submit region end(Prohibit modification and deletion)
