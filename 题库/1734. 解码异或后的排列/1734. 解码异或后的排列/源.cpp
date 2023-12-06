
#include <stdio.h>
#include <stdlib.h>

int* decode(int* encoded, int encodedSize, int* returnSize) {
	int total = 0; //totalǰn�����������Ľ����
	int odd = 0;  //ԭ����perm����һ���������Ľ����Ҳ����encodedȫ�����Ľ��
	int n = encodedSize + 1;  //perm����
	int* perm = (int*)malloc(sizeof(int) * n);  //����n��int�Ĵ洢�ռ䣬���ص�һ���ĵ�ַ
	int i;

	for (i = 1; i <= n; i++)
		total ^= i;
	for (i = 1; i < encodedSize; i+=2)
		odd ^= encoded[i];

	perm[0] = total ^ odd;
	//printf("%d \n", perm[0]);
	for (i = 0; i < encodedSize ; i++)
	{
		perm[i + 1] = perm[i] ^ encoded[i];
		//printf("%d ", perm[i + 1]);
	}
	*returnSize = n;
	return perm;
}

int main()
{
	int a[] = { 3,1 };
	int b[] = { 6,5,4,6 };
	int sza = sizeof(a) / 4;
	int szb = sizeof(b) / 4;
	int i;
	int* perm;
	int sz = 0;
	perm = decode(a, sza, &sz);
	for (i = 0; i < sz; i++)
	{
		printf("%d ", *(perm + i));
	}
	printf("\n\n");
	perm = decode(b, szb, &sz);
	for (i = 0; i < sz; i++)
	{
		printf("%d ", *(perm + i));
	}return 0;
}


/*
1734. �������������
����һ����������?perm?������ǰ?n?�������������У���?n?�Ǹ� ����?��

�������ܳ���һ������Ϊ n - 1?����������?encoded?������?encoded[i] = perm[i] XOR perm[i + 1]?���ȷ�˵�����?perm = [1,3,2]?����ô?encoded = [2,1]?��

����?encoded?���飬���㷵��ԭʼ����?perm?����Ŀ��֤�𰸴�����Ψһ��

?

ʾ�� 1��

���룺encoded = [3,1]
�����[1,2,3]
���ͣ���� perm = [1,2,3] ����ô encoded = [1 XOR 2,2 XOR 3] = [3,1]
ʾ�� 2��

���룺encoded = [6,5,4,6]
�����[2,4,1,5,3]
?

��ʾ��

3 <= n <?105
n?��������
encoded.length == n - 1

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/decode-xored-permutation
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
*/