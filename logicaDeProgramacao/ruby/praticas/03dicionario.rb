
# inicializando dicionários vazios
dicionario = {}
dicionario1 = Hash.new

puts dicionario, dicionario1

#criando e imprimindo dicionario
dicionario3 = {nome: "Ezequiel", idade: 32}
puts dicionario3 #imprime o dicionário completo
puts dicionario3[:nome] #imprime apenas o valor da chave nome

dicionario3[:altura] = 1.77 #adicione a chave altura e o valor 1.77 ao dicionario3
puts dicionario3

dicionario4 = {altura: 1.77, signo: "Aquário", time: "Santa Cruz FC"}

puts dicionario3 == dicionario4

dicionario3.delete(:altura) #deleta a chave altura
puts dicionario3.has_key?(:nome_completo) #testa se dicionario3 tem a chave nome_completo

puts dicionario3.keys #imprime as chaves de dicionario3
puts dicionario3.size #imprime o tamanho de dicionario3
puts dicionario3.length #imprime o comprimento do dicionario3

