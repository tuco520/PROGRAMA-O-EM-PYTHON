def atividade_1():
    try:
        n = int(input('digite um numero: '))
    except ValueError as erro:
        print(erro)
        
#atividade_1()
        
def atividade_2():
   try:
    n1 = int(input('n1: '))
    n2 = int(input('n2: '))
    
    div = n1/n2
   except ZeroDivisionError as code:
       print(code)
       
# atividade_2()

def atividade_3():
   try:
    lista =[1,4,6,8]
    i = int(input('digite o index: '))
    print (lista[i])
   except IndexError as erro:
        print (erro)
           
atividade_3()