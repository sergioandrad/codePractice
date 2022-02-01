/*
Autor: Sergio Andrade
Data: 27/01/2021
Titulo: ATM
Descricao: Encontra a decomposição mínima de um número usando a base (50,10,5,1).
*/

# include <stdio.h>

int main(){
    int val,c50=0,c10=0,c5=0,c1=0;
    scanf("%d", &val);
    c50 = (int) val/50;
    if(val-c50*50 > 0){
        c10 = (int) (val-c50*50)/10;
        if(val-c50*50-c10*10 > 0){
            c5  = (int) (val-c50*50-c10*10)/5;
            if(val-c50*50-c10*10-c5*5 > 0){
                c1  = (int) (val-c50*50-c10*10-c5*5);
            } 
        }
    } 
    printf("%d %d %d %d", c50,c10,c5,c1);  
}