from decimal import Decimal, getcontext
from datetime import datetime
import calendar

print("*************************************************************************")
print("Bem vindo(a) ao Calculo de Férias [Brasil]")
print("*************************************************************************")

def calculo_ferias():
    salario_sr = input("Informe seu salário bruto: ")
    salario_sr = salario_sr.replace(',', '.')
    salarioBruto = Decimal(salario_sr)
    
    diasFerias_str = input("Quantos dias de férias: ")
    diasFerias = int(diasFerias_str)
    
    valorPorDia = salarioBruto / 30
    
    valorFerias = valorPorDia * diasFerias
    
    print(f"Valor das férias para {diasFerias} dias é de R${valorFerias:.2f}")
    
calculo_ferias()