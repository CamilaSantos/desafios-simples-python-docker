print("*************************************************************************")
print("Bem vindo(a) ao conversor de temperatura (Celsius para Fahrenheit)")
print("*************************************************************************")



def conversor_temperatura():
    
    celsius_str = input("Informe a temperatura Celsius: ")
    celsius = int(celsius_str)
    
    conversor = celsius * 1.8 + 32
    
    print(f"Temperatura convertida em Fahrenheit: {conversor}")
    
conversor_temperatura()