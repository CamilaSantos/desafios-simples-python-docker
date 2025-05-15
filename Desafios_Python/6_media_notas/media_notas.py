def media_nota():
    quantidadeMinima = 3
    listaNota = []
    
    while len(listaNota) < quantidadeMinima:
        notas = input("Informa uma nota: ")
        try:
            notas_float = float(notas.replace(',','.'))
            listaNota.append(notas_float)
            print(f"Notas {notas_float} adicionada com sucesso!")
        except:
            print("Entrada inválida! Por favor, digite um número (ex.: 2, 2.2, 2,2)")    
    if len(listaNota) == quantidadeMinima:
            qtdLista = len(listaNota)
            media = sum(listaNota)/qtdLista
            return media    
    else:
        mensagemErro =  print(f"Não foi possível calcular a méndia das notas {listaNota} informada.")

resultado = media_nota()
print(f"Sua média de nota é {resultado}")