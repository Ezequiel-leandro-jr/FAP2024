# IMPRESSÃO E ATRIBUIÇÃO DE VALORES EM VARIÁVEIS #

puts "Olá! Digite seu nome:"
nome = gets.chomp
puts "Muito prazer em conhecê-lo, #{nome}! Agora, me diga a sua idade:"
idade = gets.chomp.to_i
puts "Entendi, você tem #{idade}..."

# OPERADORES NUMÉRICOS BÁSICOS #
puts "Digite um número inteiro:"
numero1 = gets.chomp.to_i
puts "Agora digite outro número inteiro:"
numero2 = gets.chomp.to_i

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

puts "A soma entre #{numero1} + #{numero2} = #{soma}"
puts "A subtração entre #{numero1} - #{numero2} = #{subtracao}"
puts "A multiplicação entre #{numero1} * #{numero2} = #{multiplicacao}"
puts "A divisão entre #{numero1} / #{numero2} = #{divisao}"

# OPERADORES BOOLEANOS #

# iguais aos JavaScript

puts false && true
puts false || true
puts false && false
puts false || false
puts !true && true

# CONDICIONAIS #

#if

if idade >= 18
  puts "Você tem #{idade} anos. É maior de idade."
end

if idade >= 20 && idade <= 30
  puts "Você tem entre 20 e 30 aninhos..."
elsif idade < 20
  puts "Você tem menos de 20 anos??"
else
  puts "Parece que você não tem entre 20 e 30 aninhos, néah..."
end

# case

puts "#{nome}, que time é teu?"
time = gets.chomp
time = time.downcase

case time
when "sport"
  puts "É burro-negro, néah hahaha"
when "náutico" || "nautico"
  puts "É a barbie dos aflitos hahahaha"
when "santa cruz"
  puts "Aí tá certo! Tricolor, porra!"
else
  puts "Sabe quem te meteu não, né, tá inventando aí hahaha"
end




