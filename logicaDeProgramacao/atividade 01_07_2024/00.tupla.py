# TUPLAS
# estruturas de dados imutáveis em Python,
# São úteis parea armazenar coleções ordenadas de itens que não precisam ser modificados

tupla = (1, 2, 3, 4, 5)
#imprimindo primeiro índice da tupla
print(tupla[0])
#iterando sobre os elementos da tupla
for lista in tupla:
    print("tupla: ", lista)

# OPERAÇÕES COMUNS COM TUPLAS #

#concatenação
tupla2 = (6, 7, 8, 9, 10)

concatenando = tupla + tupla2

for lista in concatenando:
    print(lista)

# EXERCÍCIO #

# Criando uma tupla para armazenar as UFs BR
ufDoBrasil = ( "AC", "AM", "AP", "MA", "CE", "RN", "PB", "PE", "PI", "AL", "SE", "BA", "ES", "RJ", "SP", "PR", "SC", "RS", "MT", "MS", "GO", "MG", "TO", "RR", "RO", "DF" )
for uf in ufDoBrasil:
    print('-', uf)