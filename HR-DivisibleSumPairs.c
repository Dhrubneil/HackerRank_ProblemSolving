/*
   Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by .

Example

ar = [1,2,3,4,5,6]

Three pairs meet the criteria: [1,4], [2,3] and [4,6].

Function Description

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array ar
int ar[n]: an array of integers
int k: the integer divisor
Returns
- int: the number of pairs

Input Format

The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers, each a value of ar[i].

CONSTRAINTS

-- 2 <= n <= 100
-- 1 <= k <= 100
-- 1 <= ar[i] <= 100


STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

Sample output : 5
*/

#include<stdio.h>

int divisibleSumPairs(int n, int k, int ar_count, int* ar) {
    int i, j;
    int pair = 0;
    for(i = 0; i < n-1; i++){
        for(j = i+1; j < n; j++){
            int sum = ar[i] + ar[j];
            if(sum % k == 0)
                pair += 1;
        }
    }
    return pair;
}

int main(){
    int n, k;
    printf("\nEnter n and k where n is the number of elements in the array and k is the divisor: ");
    scanf("%d %d", &n, &k);
    int ar[n];

    int i;
    printf("\nEnter %d elements: \n", n);
    for(i = 0; i < n; i++){
        scanf("%d", &ar[i]);
    }

    printf("\nElements: %d\tDivisor: %d\n", n, k);
    printf("\nArray elements are: ");
    for(i = 0; i < n; i++){
        printf("%d ", ar[i]);
    }
    printf("\n");

    int result = divisibleSumPairs(n, k, n, ar);
    printf("\nThere are %d pair(s)\n", result);
}
