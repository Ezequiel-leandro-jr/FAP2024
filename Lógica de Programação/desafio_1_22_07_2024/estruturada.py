import os
import time
lista_carros = []
indice = 1 


def imprimir(indice):
    for carro in lista_carros:
        if carro["indice"] == indice:
            print(f'''
            -----------------------------------------------------------------------
            N°: {carro["indice"]} MARCA: {carro["marca"]} MODELO: {carro["modelo"]}
                                  ANO: {carro["ano"]}     COR: {carro["cor"]}
            -----------------------------------------------------------------------''')

def cadastrar(indice):
    print('=== cadastro ===\n')
    marca = input('Digite a marca do carro: ')
    modelo = input('Digite o modelo do carro: ')
    ano = int(input('Digite o ano do carro: '))
    cor = input('Digite a cor do carro: ')
    carro = dict(indice=indice, marca=marca, modelo=modelo, ano=ano, cor=cor, motor=False)
    return carro

def ligar_desligar(indice):
    
    for carro in lista_carros:
        if carro["indice"] == indice:
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
    1. Cadastrar
    0. Sair
    ____________________''')

def main(indice):
    while True:
        cabecalho()
        op = int(input('>> '))
        match op:
            case 1:
                carro = cadastrar(indice)
                indice = indice + 1
                lista_carros.append(carro)
                imprimir(carro["indice"])
                ligar_desligar(carro["indice"])
            case 0:
                print('Saindo do sistema. Volte sempre...')
                break

if __name__ == "__main__":
    main(indice)