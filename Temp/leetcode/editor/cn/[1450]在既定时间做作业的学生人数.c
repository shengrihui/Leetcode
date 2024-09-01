// 1450 在既定时间做作业的学生人数
// https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/


//leetcode submit region begin(Prohibit modification and deletion)
int busyStudent(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int queryTime) {
    int ans = 0;
    for(int i = 0; i < startTimeSize; i++){
        if(startTime[i] <= queryTime && queryTime <= endTime[i])
            ans++;
    }
    return ans;
}
/*
int busyStudent(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int queryTime) {
    int* diff = (int*)malloc(1010 * 4);
//    for(int i = 0;i < 1010; i++){
//        diff[i] = 0;
//    }
    memset(diff, 0, 1010 * 4);
    for(int i = 0; i < startTimeSize; i++){
        diff[startTime[i]]++;
        diff[endTime[i] + 1]--;
    }
    for(int i = 1; i <= queryTime; i++){
        diff[i] += diff[i - 1];
    }
    int ans = diff[queryTime];
    free(diff);
    return ans;
}
*/
//leetcode submit region end(Prohibit modification and deletion)
