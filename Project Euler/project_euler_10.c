#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#include <stdio.h>
#include <math.h>




int asal_mi(int a){
    int i;
for(i = 2; i <= sqrt(a); i++){
    if(a%i==0){
        return 0;
    }
    else{
        ;
    }
}
return 1;
}

int main()
{
int sayi,c=2000000;
long long toplam=0;

for(sayi = 2; sayi < c; sayi++){

    if(asal_mi(sayi)==1){
        toplam += sayi;
        printf("\n%d \ttoplam=%lld",sayi,toplam);
    }

}



return 0;


}
