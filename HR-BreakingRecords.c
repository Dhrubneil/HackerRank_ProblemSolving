#include<stdio.h>
#include<stdlib.h>

int* RecordBreaks(int scores[], int score_count, int* result_count){
    result_count = (int*)calloc(2,sizeof(int));
    int min = scores[0];
    int max = scores[0];
    int i;

    for(i = 1; i < score_count; i++){
        if(scores[i] < min){
            min = scores[i];
            result_count[1] += 1;
        }
        else if(scores[i] > max){
            max = scores[i];
            result_count[0] += 1;
        }
    }
    return result_count;
}

int main(){
    int n;
    printf("Enter number of games: ");
    scanf("%d", &n);
    int scores[n];
    int i;
    printf("Enter scores of the %d games respectively : ", n);
    for(i = 0; i < n; i++){
        scanf("%d", &scores[i]);
    }

    for(i = 0; i < n; i++){
        printf("%d ", scores[i]);
    }
    int result_count;

    int *result = RecordBreaks(scores, n, &result_count);

    printf("\n\n");
    for(i = 0; i < 2; i++){
        printf("%d ", *(result+i));
    }
}
