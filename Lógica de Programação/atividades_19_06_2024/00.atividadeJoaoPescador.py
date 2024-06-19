multa = 0
pesoPeixes = float(input('Digite o peso da pesca em Kg: '))

excesso = pesoPeixes - 50

if pesoPeixes > 50:
    multa = excesso * 4

print(f'\nPeso da pesca: {pesoPeixes:.2f}kG\nPeso em excesso: {excesso:.2f}KG\nValor da multa: R${multa:.2f}')

