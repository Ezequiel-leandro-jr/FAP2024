# DICIONÁRIOS
# estruturas de dados que mapeiam chaves e valores
# eficientes para buscas rápidas e associações de informações

# Operações comuns com dicionários #

dicionario = {"chave1": 1, "chave2": 2, "chave3": 3}
print(dicionario)
#acessando valor pela chave
print('\nAcessando o valor da "chave1" pela chave: ', dicionario["chave1"])
#adicionando novo par chave-valor
dicionario["chave4"] = 4
print('\nAdicionamos um novo par chave-valor = "chave4": 4')
print(dicionario)
#Iterando sobre as chaves
print('Iterando e imprimindo as chaves: valores através do for in:')
for lista in dicionario.items():
    print(lista)

print('Iterando e imprimindo os valores através do for in:')
for lista in dicionario.values():
    print(lista)

print('Iterando e imprimindo as chaves através do for in:')
for lista in dicionario:
    print(lista)


