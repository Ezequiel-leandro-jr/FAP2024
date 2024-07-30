# LISTAS, ARRAYS OU VETORES #
lista = []
puts "Digite o valor do primeiro elemento:"
elemento = gets.chomp
lista.push(elemento)
puts "Digite o valor do segundo elemento:"
  elemento = gets.chomp
  lista.push(elemento)
  puts "Os elementos da lista são: #{lista[0]} e #{lista[1]}"
  puts "Digite o valor do terceiro elemento:"
  elemento = gets.chomp
  lista << elemento
  puts "Os elementos da lista agora são: #{lista[0]}, #{lista[1]} e #{lista[2]}"
  puts "Digite o valor do quarto elemento:"
  elemento = gets.chomp
  puts "Agora, digite a posição na lista que você quer alocá-lo <1, 2, 3, 4>:"
  indice = gets.chomp.to_i
  lista.insert(indice, elemento)
  puts "Os 4 elementos da lista agora são: #{lista[0]}, #{lista[1]}, #{lista[2]}, #{lista[3]}, #{lista[4]}"


