print("*******************************************")
print("Bem vindo(a) à Tabuada!")
print("*******************************************")

def tabuada():
    
    
    numero_escolhido = input("Informe um número de 0 à 10: ")
    numero = int(numero_escolhido)
    try:
        
        if numero < 0 or  numero > 10:
            print("Valor Inválido!")       
        else: 
            print(f"Tabuada do {numero}:")   
            for multiplicador in range(0,11):
                resultado = int(numero) * multiplicador
                print(f"|{numero}x{multiplicador} = {resultado}|")
    except:
        print("Entrada inválida. Por favor, digite um número inteiro.")               

tabuada()