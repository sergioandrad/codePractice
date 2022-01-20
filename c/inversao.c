# include <stdio.h>

int main(){
    int num1,a,b,c,num2;
    scanf("%d", &num1);
    a = num1 % 10;
    b = ((num1 % 100) - a)/10;
    c = (num1 -a -b)/100;
    num2 = a*100 + b*10+ c;
    printf("%d", num2);
    }