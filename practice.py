##################################################################################
# checkCardNumber
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Utilizando regex para identificar se um número é um número de cartão
# de crédito sob as seguintes restrições:
# i. Começa com 4, 5 ou 6.
# ii. Contem 16 digitos.
# iii. Possivelmente dividio por hifens
# iv. Nao contem outros separadores como ' ' e '_'.
# v. Nao contem 4 ou mais digitos consecutivos repetidos.
##################################################################################

dados = input().split(sep='\n')
del dados[0]   

import re
pattern = re.compile(pattern = '[456]\d{15}|[456]\d{3}(-\d{4}){3}')
consec  = re.compile(pattern = '(.)\\1{3,}')
 
def checkCardNumber(s):
    check = pattern.match(s) != None and consec.search(s.replace('-','').replace(' ','')) == None
    if check == True: 
        print('Valid') 
    else: 
        print('Invalid')
 
for i in dados:
    checkCardNumber(i)


##################################################################################
# swapCases
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Troca letras maisculas por minusculas e vice-versa.
##################################################################################

def swapCases(s):
    t   = 0
    new = ''
    for i in s:
        if i.islower() == True:
            new = new + s[t].capitalize() 
        else:
            new = new + s[t].lower()
        t += 1    
    return new

string = 'Hello World'
swapCases(string)

##################################################################################
# checkString
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Checa que tipos de caracteres uma string contém
# usando list comprehesion.
##################################################################################

def checkString(s): 
    from numpy  import empty
    from pandas import DataFrame
    check = empty((5,1))
    check[0,0] = len([x for x in s if x.isalnum()==True])!= 0
    check[1,0] = len([x for x in s if x.isalpha()==True])!= 0
    check[2,0] = len([x for x in s if x.isdigit()==True])!= 0
    check[3,0] = len([x for x in s if x.islower()==True])!= 0
    check[4,0] = len([x for x in s if x.isupper()==True])!= 0
    return DataFrame(check).rename(
        index = {0:'alnum', 1:'alpha', 2:'digit', 3:'lower', 4:'upper'},
        columns = {0:'teste'})

string2 = 'Hello World2'
checkString(string2)



##################################################################################
# createFig
# Autor: Sergio Henrique Andrade de Azevedo;
# Descricao: Criando figuras ASCII, toma as dimensoes da figura e
# retorna a figura no console.
##################################################################################

def createFig(N,M):
    chars = 1
    for i in range(N+1):
        if i < N/2-1:
            n = (M-chars*3)/2
            print('-'*int(n) + '.|.'*int(chars) + '-'*int(n))
            chars += 2
        if i == (N-1)/2+1:
            tr = (M-7)/2
            chars = M/3-2 
            print('-'*int(tr) + 'WELCOME' +'-'*int(tr))     
        if i > (N-1)/2+1:
            n = (M-chars*3)/2
            print('-'*int(n) + '.|.'*int(chars) + '-'*int(n))    
            chars -= 2

dim = input().split()
createFig(int(dim[0]),int(dim[1]))
















       