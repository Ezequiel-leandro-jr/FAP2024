def soma(n1, n2):
    soma = n1 + n2
    print(f"{n1:.1f} + {n2:.1f} = {soma:.1f}")

op = 1

while(op == 1):
    print('\n=== SOMA ENTRE DOIS NÚMEROS ===\n')
    n1 = float(input('Digite o primeiro numero da soma: '))
    n2 = float(input('Digite o segundo numero da soma: '))
    soma(n1, n2)
    op = int(input('Deseja realizar nova soma? <1-sim | 2-nao>'))

print('Programa finalizado com sucesso!!!')




