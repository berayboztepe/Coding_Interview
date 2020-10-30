#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=300,b=300,x,y,z,q,w,e;
    long int sonuc;

    while(a<1000){
        b=300;
        while(b<1000){
                sonuc=a*b;
                x=sonuc/100000;
                y=(sonuc-(x*100000))/10000;
                z=(sonuc-(y*10000)-(x*100000))/1000;
                q=(sonuc-(z*1000)-(y*10000)-(x*100000))/100;
                w=(sonuc-(q*100)-(z*1000)-(y*10000)-(x*100000))/10;
                e=(sonuc-(w*10)-(q*100)-(z*1000)-(y*10000)-(x*100000));
                if(x==e && y==w && z==q){
                        printf("a=%d*b=%d=%d\n ",a,b,sonuc);
                        b++;
                    }
                    else{
                        b++;
                    }
        }

        a++;
    }


return 0;


}
