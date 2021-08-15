#include<stdio.h>


int birthday(int s_count, int* s, int d, int m) {
    int i,j;
    if(s_count == 1 && s[0] == d && m == 1){
        return 1;
    }
    //else return NULL;
    int sum = 0;
    int way = 0;
    for(i = 0; i < s_count; i++){
        sum = s[i];
        for(j = i+1; j <= i+m-1; j++){
            sum += s[j];
            if(sum > d)
                break;
        }
        if(sum == d)
            way += 1;
    }
    return way;
}

int main(){
    printf("How many blocks are there in the chocolate bar? ");
    int n;
    scanf("%d", &n);
    int i;
    int arr[n];
    printf("Enter the numbers inscribed in the blocks.\n");
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    int month, day;
    printf("Enter birth day and month: ");
    scanf("%d %d", &day, &month);
    printf("The numbers in the blocks are: ");
    for(i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    printf("\nBirth day = %d\tBirth month = %d\n", day, month);

    int result = birthday(n, arr, day, month);
    printf("\nResult = %d\n", result);
}
