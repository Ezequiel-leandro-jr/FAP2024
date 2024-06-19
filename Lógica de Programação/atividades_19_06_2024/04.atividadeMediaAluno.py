print('\t\n===COLÉGIO SOFTEX===\n')

notas = []
somatorio = 0

qtd = int(input('Digite a quantidade de notas a serem processadas: '))

for i in range(0,qtd):
    n = float(input(f'Digite a {i+1}° nota: '))
    notas.append(n)
    somatorio += notas[i]

print('\t\n---NOTAS DO(A) ALUNO(A)---')
for i in range(0,qtd):
    print(f'NOTA {i+1} = {notas[i]:.2f}')
if somatorio/qtd > 10:
    print(f'MÉDIA: {somatorio/qtd:.2f}\nSITUAÇÃO: ERRO NAS NOTAS. TENTE NOVAMENTE.')
elif somatorio/qtd == 10:
    print(f'MÉDIA: {somatorio/qtd:.2f}\nSITUAÇÃO: APROVADO(A) COM DISTINÇÃO!!')
elif somatorio/qtd >= 7:
    print(f'MÉDIA: {somatorio/qtd:.2f}\nSITUAÇÃO: APROVADO(A)!!')
elif somatorio/qtd < 7 and somatorio/qtd >= 0 :
    print(f'MÉDIA: {somatorio/qtd:.2f}\nSITUAÇÃO: REPROVADO(A)!!')
else:
    print(f'MÉDIA: {somatorio/qtd:.2f}\nSITUAÇÃO: ERRO NAS NOTAS. TENTE NOVAMENTE.')








