#The sum of the squares of the first ten natural numbers is,

#1^2+2^2+...+10^2=385
#The square of the sum of the first ten natural numbers is,

#(1+2+...+10)^2=55^2=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#include <stdio.h>
#include <stdlib.h>

int main()
{
int i,toplam1=0,toplam2=0,cevap;

for(i=0;i<=100;i++){
    toplam1+=(i*i);
}

for(i=0;i<=100;i++){
    toplam2+=i;

}
cevap=((toplam2*toplam2)-toplam1);

printf("%d %d %d",toplam1,toplam2,cevap);



return 0;


}
