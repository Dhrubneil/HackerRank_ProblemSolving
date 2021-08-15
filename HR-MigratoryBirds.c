#include<stdio.h>
#include<math.h>


//The following code terminates due to timeout while submitting in HR-portal
//Time limit exceeded, need optimization
int migratoryBirds(int arr_count, int* arr) {
    int i, j, max;
    int bird = arr[0];
    max = 1;
    for(i = 0; i < arr_count; i++){

        int count = 1;
        for(j = i+1; j < arr_count; j++){
            if(arr[i] == arr[j]){
                count += 1;
                if(count > max){
                    max = count;
                    bird = arr[i];
                }
            }
        }
        if(count == max && arr[i] < bird){
            bird = arr[i];
        }
    }
    return bird;
}


/*As I didn't notice carefully that the bird ids are guaranteed to be 1,2,3,4 and 5, I wrote the code above which
is fine but cost O(n*n) time

Now, as it is convenient to map the travel count of a bird to it's index, i.e. a new array named travel_cost of size 6
(as index 0 cannot be mapped to any of the bird's id that is in range[1,5]) can be declared to store the time(s) a bird
traveled

Thus, the code is now optimized and executed within time limit
*/
int mgrtBrd(int arr_count, int* arr){
    int travel_count[6] = {};
    int max = 0;
    int bird_n = 0;
    int i, id;
    for(i = 0; i < arr_count; i++){
        id = arr[i];
        travel_count[id] += 1;

        if(travel_count[id] > max){
            max = travel_count[id];
            bird_n = id;
        }
        else if(travel_count[id] == max){
            bird_n = (int)fmin(bird_n, id);
        }
    }
    return bird_n;
}

int main(){
    int n;
    printf("\nEnter the number of travels: ");
    scanf("%d", &n);
    int bird_id[n];
    printf("\nEnter bird's id: \n");
    int i;
    for(i = 0; i < n; i++){
        scanf("%d", &bird_id[i]);
    }

    printf("\nBird ids are: ");
    for(i = 0; i < n; i++){
        printf("%d ", bird_id[i]);
    }
    printf("\n");

    int result = migratoryBirds(n, bird_id);

    printf("\n%d\n", result);

    result = mgrtBrd(n, bird_id);

    printf("\n-->%d\n", result);
}
