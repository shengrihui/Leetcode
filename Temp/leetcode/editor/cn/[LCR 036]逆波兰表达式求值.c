// LCR 036 逆波兰表达式求值
// https://leetcode.cn/problems/8Zf90G/

//leetcode submit region begin(Prohibit modification and deletion)
#include <string.h>
#include <stdlib.h>
bool isNum(char* token){
    return strlen(token) > 1 ||  token[0] <= '9' &&  token[0] >= '0';
}
int evalRPN(char** tokens, int tokensSize){
    int st[tokensSize], top = 0;
    for(int i = 0; i < tokensSize; i++){
        char* token = tokens[i];
        if (isNum(token)){
            st[top++] = atoi(token);
        }else{
            int num2 = st[--top];
            int num1 = st[--top];
            switch (token[0]){
                case '+':
                    st[top++] = num1 + num2;
                    break;
                case '-':
                    st[top++] = num1 - num2;
                    break;
                case '*':
                    st[top++] = num1 * num2;
                    break;
                case '/':
                    st[top++] = num1 / num2;
                    break;
            }
        }
    }
    return st[0];
}
//leetcode submit region end(Prohibit modification and deletion)
