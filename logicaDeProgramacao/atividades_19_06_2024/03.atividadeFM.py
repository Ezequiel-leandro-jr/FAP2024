
op = True
while(op):
    letra = input('Digite o seu sexo < F | M >: ')
    letra = letra.lower()
    if letra == 'm':
        print('Seu sexo é MASCULINO.')
        op = False
    elif letra == 'f':
        print('Seu sexo é FEMININO.')
        op = False
    else:
        print('\n<<Letra inválida! Tente novamente!>>\n')


