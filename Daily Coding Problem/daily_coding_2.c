#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int n;
    printf("How many numbers will be in array?");
    scanf("\n%d", &n);
    int array[n];

    printf("\nPlease input numbers:");

    for(int i = 0; i<n; i++){
        scanf("%d", &array[i]);
    }

    deneme(array, n);


}

void deneme(int array[], int n){
    int newarray[n];
    for(int i = 0; i<n;i++){
        newarray[i] = 1;
    }
    for(int i = 0; i<n; i++){
        for(int j = 0; j<n; j++){
            if(j == i);
            else{
                newarray[i] *= array[j];
            }
        }
    }
    for(int i = 0; i<n;i++){
        printf("\n%d\n", newarray[i]);
    }
}
