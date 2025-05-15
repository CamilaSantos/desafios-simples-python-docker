def lista_de_compras():
    
    print("**********************************************")
    print("Seja bem-vindo(a) a Lista de Compras - Simples")
    print("**********************************************")
    
    lista = []
    quantidadeMinima = 5
    
    while len(lista) < quantidadeMinima:
        item = input("Informe o itém: ")
        lista.append(item)
        print(f"Item {item} adicionado com sucesso!")
    
    print(f"A lista atingiu o número minímo de {quantidadeMinima}")
    print(f"Itens adicionados: {lista}")
   
lista_de_compras()
