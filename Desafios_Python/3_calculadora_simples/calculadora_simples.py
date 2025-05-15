import pdb

num1 = 1
num2 = 2
num3 = 3
num4 = 4

print("*********************************************")
print("Seja bem-vindo(a) ao Calculadora Simples :)")
print("*********************************************")

def calculadora_simples():

    operacao_str = input("Selecione: 1-Soma(+), 2-Subtração(-), 3-Multiplicação(*) ou 4-Divisão(/): ")

    try:
        operacao = int(operacao_str)
    except ValueError:
        print("Operação inválida!")
        return None

    if operacao != num1 and operacao != num2 and operacao != num3 and operacao != num4:
        print("Operação inválida!")
        return None

    else:
        valor1_str = input("informe o primeiro valor: ")
        valor2_str = input("informe o segundo valor: ")

        if valor1_str == "" or valor2_str == "":
            print("Valor inválido!")
            return None

        try:
            valor1 = int(valor1_str)
            valor2 = int(valor2_str)
        except ValueError:
            print("Valor inválido!")
            return None

        if operacao == num1:
            soma = valor1 + valor2
            print(f"Resultado de {valor1} + {valor2} = {soma}")
            return soma

        elif operacao == num2:
            subtracao = valor1 - valor2
            print(f"Resultado de {valor1} - {valor2} = {subtracao}")
            return subtracao

        elif operacao == num3:
            multiplicacao = valor1 * valor2
            print(f"Resultado de {valor1} * {valor2} = {multiplicacao}")
            return multiplicacao

        elif operacao == num4:
            if valor2 == 0:
                print("Erro: Divisão por zero!")
                return None
            else:
                divisao = valor1 / valor2
                print(f"Resultado de {valor1} / {valor2} = {divisao}")
                return divisao

resultado = calculadora_simples()
print(f"{resultado}")