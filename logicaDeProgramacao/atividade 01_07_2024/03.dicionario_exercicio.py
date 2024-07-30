# EXERCÍCIO DE CLASSE #

#função match case para as operações do menu
def menu(op):
    match op:
        case 1:
            chave = input('Digite a sigla da UF: ')
            chave = chave.upper()
            valor = input('Digite o nome da UF por extenso: ')
            ufs[chave] = valor
        case 2:
            print('Qual UF deseja alterar?\n----------------------')
            for uf in ufs:
                print(uf)
            num = input('>> ')
            num = num.upper()
            chave = input('Digite a sigla da UF: ')
            chave = chave.upper()
            ufs[chave] = ufs.pop(num)
            valor = input('Digite o nome da UF por extenso: ')
            ufs[chave] = valor
            print('Alteração realizada com sucesso:')
        
        case 3:
            print('Qual UF deseja remover?\n----------------------')
            for uf in ufs:
                print(uf)
            num = input('>> ')
            num = num.upper()
            try:
                del ufs[num]  
            except KeyError:
                print('Esta UF não existe. Tente novamente!')
                pass  

#criando dicionário que armazena UF e sua descrição 
ufs = {
    "AC": 'Acre',
    "AM": 'Amazonas',
    "AP": 'Amapá',
    "MA": 'Maranhão',
    "CE": 'Ceará',
    "RN": 'Rio Grande do Norte',
    "PB": 'Paraíba',
    "PE": 'Pernambuco',
    "PI": 'Piauí',
    "AL": 'Alagoas',
    "SE": 'Sergipe',
    "BA": 'Bahia',
    "ES": 'Espírito Santo',
    "RJ": 'Rio de Janeiro',
    "SP": 'São Paulo',
    "PR": 'Paraná',
    "SC": 'Santa Catarina',
    "MT": 'Mato Grosso',
    "MS": 'Mato Grosso do Sul',
    "GO": 'Goiás',
    "MG": 'Minas Gerais',
    "TO": 'Tocantins',
    "RR": 'Roraima',
    "RO": 'Rondônia',
    "DF": 'Distrito Federal',
}

# criando um menuzin maroto
op = 8

while op != 0:
    print('\n\tGERENCIAMENTO DE UF\n\t-------------------\nQue operação deseja realizar?\n1- Inserir nova UF e descrição\n2- Editar UF existente\n3- Remover UF existente\n4- Listar uma UF\n5- Listar tudo\n0- Sair\n------------------------------')
    op = int(input('OP: '))
    menu(op)
    

