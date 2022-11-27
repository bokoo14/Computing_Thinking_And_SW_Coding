#include <stdio.h>


void main(){
    int a=1;
    int b=1;

    for (int i=1; i<1234567; i++){
        a=a*i;
    }

    print("%d", a);
}