#include <stdio.h>

/*
Titulo: repord.c
Descricao: Lista e ordena numeros repetidos
Data:  11/02/2022
*/
int main(){
    int val[30], rep[30], ordered[30], iter=0, iter2=0,checkrep=0,score=0;
    val[iter]=1;
    for (size_t i = 0; i < 30; i++)
    {
        rep[i]=0;
    }
    while (val[iter] !=0)
    {   
        iter++;
        scanf("%d", &val[iter]);
        if(val[iter]==0){break;}    
    }
    for (size_t i = 0; i < iter; i++)
    {
        checkrep=0;
        for (size_t j = i+1; j < iter; j++)
        {
            for (size_t k = 0; k < iter2; k++)
                {
                    if(val[i]==rep[k]){checkrep=1;}
                }
                if (checkrep==1)
                {
                    continue;
                }
            if(val[i]==val[j]){
                rep[iter2]=val[i];
                iter2++;
            }
        }
    }

    for (size_t j = 0; j < iter2; j++)
    {
        score = iter2-1;
        for (size_t i = 0; i < iter2; i++)
        {   
            if (rep[j] < rep[i]){score--;}
            if (rep[j] == rep[i] && j != i)
            {
                if(j>i){continue;}else{score--;}
            }
            
        }
        ordered[score]=rep[j];
    }
    for (size_t i = 0; i < iter2; i++)
    {
        printf("%d\n",ordered[i]);
    }
}