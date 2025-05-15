par = [2,4,6,8,0]
impar  = [1,3,5,7,9]

def par_ou_impar():
    print("Validando se o número é PAR ou IMPAR ")
    num = input("Informe um número:")
    ultimo_valor = int(num) % 10
    
    if not(ultimo_valor in par or ultimo_valor in impar):
        return f"Valor digitado {num} inválido!"
    
    if ultimo_valor in par:
        return "PAR"
    
    return "IMPAR"

resultado = par_ou_impar()
print(resultado)