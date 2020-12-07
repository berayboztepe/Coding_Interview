#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sayi,i,d=0,a=1;

for(sayi=2;;sayi++){
    for(i=2;i<sayi;i++){
        if(sayi%i==0){
            d=0;
            break;
            }
        else{
                d=1;
            }
        }
    if(d==1){
        a+=1;
        if(a==10001){
            printf("%d'inci sayi=%d\n",a,sayi);
            break;
            }

        }

    }


return 0;


}
