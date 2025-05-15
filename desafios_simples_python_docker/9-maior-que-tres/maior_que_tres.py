print("*******************************************************************************")
print("Bem vindo(a) Vamos descubrir qual o maior número que você digitou!")
print("*******************************************************************************")

def maior_que_tres():
   
   try:
        listaNumero = []
        
        
        for i in range (3):
            numero_str = input(f"Informe o {i+1}° número: ") 
            numero = int(numero_str)
            listaNumero.append(numero)
            print(f"Números adicionados: {listaNumero}")               
             
               
        if listaNumero:       
            oMaior = max(listaNumero)
            print(f"\nOs números digitados foram: {listaNumero}")
            print(f"O maior número é: {oMaior}")
        else:
            print("\nNenhum número foi informado.")

   except ValueError:
        print("Valor informado é inválido! Por favor, digite um número inteiro.")
   except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
       
       
maior_que_tres()