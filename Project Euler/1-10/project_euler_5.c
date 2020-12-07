#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,i;

    for(a=2520;;a++){
        if(a%2==0){
            if(a%3==0){
                if(a%4==0){
                    if(a%5==0){
                        if(a%6==0){
                            if(a%7==0){
                                if(a%8==0){
                                    if(a%9==0){
                                        if(a%10==0){
                                            if(a%11==0){
                                                if(a%12==0){
                                                    if(a%13==0){
                                                        if(a%14==0){
                                                            if(a%15==0){
                                                                if(a%16==0){
                                                                    if(a%17==0){
                                                                        if(a%18==0){
                                                                            if(a%19==0){
                                                                                if(a%20==0){
                                                                                    printf("%d",a);
                                                                                    break;
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        }


    return 0;
}
