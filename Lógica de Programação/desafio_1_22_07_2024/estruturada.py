import os
import time
lista_carros = []



def imprimir(placa):
    for carro in lista_carros:
        if carro["placa"] == placa:
            print(f'''
            -----------------------------------------------------------------------
            N°:{carro["placa"]} MARCA:{carro["marca"]} MODELO:{carro["modelo"]}
            ANO:{carro["ano"]} COR:{carro["cor"]}
            -----------------------------------------------------------------------''')

def cadastrar():
    op = 1
    while op == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('=== CADASTRO ===\n')
        placa = input('DIGITE A PLACA DO CARRO: ')
        marca = input('DIGITE A MARCA DO CARRO: ')
        modelo = input('DIGITE O MODELO DO CARRO: ')
        ano = int(input('DIGITE O ANO DO CARRO: '))
        cor = input('DIGITE A COR DO CARRO: ')
        carro = dict(placa=placa, marca=marca, modelo=modelo, ano=ano, cor=cor, motor=False)
        lista_carros.append(carro)
        
        op = 3
        while op != 1 or op != 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('=== CADASTRO ===\n')
            print('CADASTRO REALIZADO COM SUCESSO!')
            imprimir(carro["placa"])
            op = int(input('''OPCAO: 
            [1] NOVO CADASTRO [2] VOLTAR AO MENU'''))
            if op == 1:
                break
            elif op == 2:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('OPCAO INVALIDA! TENTE NOVAMENTE!')
                time.sleep(2)

def ligar_desligar(placa):
    
    for carro in lista_carros:
        if carro["placa"] == placa:
            motor = carro["motor"]
            
    op = int(input('''
    Escolha uma opcao abaixo:

    1.Ligar motor  2.Desligar motor  3.Voltar ao Menu
    
    >> '''))

    match op:
        case 1:
            if motor == True:
                opcao = int(input("O motor do carro já está ligado! Digite 1 para desligar ou qualquer outro valor para voltar ao Menu: "))
                if opcao == 1:
                    motor = False
                    print('O motor agora está desligado.')
                    time.sleep(2)
            else:
                motor = True
                print(f"Motor ligado. Funcionando corretamente.")
                time.sleep(2)
        case 2:
            if motor == False:
                opcao = int(input("O motor do carro já está desligado! Digite 1 para ligar ou qualquer outro valor para voltar ao Menu: "))
                if opcao == 1:
                    motor = True
                    print('O motor agora está ligado.')
                    time.sleep(2)
            else:
                motor = False
                print("Motor desligado.")
                time.sleep(2)
        case 3:
            print('voltando ao menu...')
            time.sleep(2)

def cabecalho():
    print('''
    CADASTRO DE VEICULOS
    --------------------
            MENU
    ____________________      
    [1] CADASTRAR
    [0] SAIR
    ____________________''')

def main():
    while True:
        cabecalho()
        op = int(input('>> '))
        match op:
            case 1:
                carro = cadastrar()
            case 0:
                print('Saindo do sistema. Volte sempre...')
                break

if __name__ == "__main__":
    main()