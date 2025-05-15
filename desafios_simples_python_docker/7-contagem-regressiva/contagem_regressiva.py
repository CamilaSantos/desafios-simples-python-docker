import time


def contagem_regressiva():
   
#    inicio = 10
#    fim = 0
#    passo = -1
#    intervalo =1

    lista_contagem = list(range(10,0,-1))
   
    print("Contagem regressiva!")
   
#    for contador in range(inicio, fim, passo):
#        print(contador)
#        time.sleep(intervalo)

    for numero in  lista_contagem:
        print(numero)
        time.sleep(1)
       
    print("Fim contagem regressiva!")
   

contagem_regressiva()