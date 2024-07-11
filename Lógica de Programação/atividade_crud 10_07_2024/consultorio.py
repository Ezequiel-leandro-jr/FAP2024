#import os 
#import msvcrt

# classe Paciente
class Paciente:
    def __init__(self, prontuario, nome, idade, sexo, cpf, data, hora, especialidade, medico, retorno):
        self.prontuario = prontuario
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.data = data
        self.hora = hora
        self.especialidade = especialidade
        self.medico = medico
        self.retorno = retorno
# lista que irá armazenar os pacientes
consultorio = []

## FUNÇÕES DO CRUD ##
def adicionar_paciente(prontuario, nome, idade, sexo, cpf, data, hora, especialidade, medico, retorno):
    paciente = Paciente(prontuario, nome, idade, sexo, cpf, data, hora, especialidade, medico, retorno)
    consultorio.append(paciente)

def buscar_paciente(prontuario):
    if prontuario:
        for paciente in consultorio:
            if paciente.prontuario == prontuario:
                return paciente
    else:
        return

def listar_pacientes():
    for paciente in consultorio:
        print(f""" 
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} | IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}
                      ______________________________________________________________________
                       """)


def atualizar_paciente(atributo, indice):
    match atributo:
        case 1:
            novo_prontuario = input('Digite o novo prontuario: ')
            consultorio[indice].prontuario = novo_prontuario
        case 2:
            novo_nome = input('Digite o novo nome completo: ')
            consultorio[indice].nome = novo_nome
        case 3:
            nova_idade = input('Digite a nova idade: ')
            consultorio[indice].idade = nova_idade
        case 4:
            novo_sexo = input('Digite o novo sexo <M ou F>: ')
            novo_sexo = novo_sexo.upper()
            consultorio[indice].sexo = novo_sexo
        case 5:
            novo_cpf = input('Digite o novo CPF (apenas numeros): ')
            consultorio[indice].cpf = novo_cpf
        case 6:
            nova_data = input('Digite a nova data da consulta (ex: 09/07/2024): ')
            consultorio[indice].data = nova_data
        case 7:
            novo_horario = input('Digite o novo horario da consulta (ex: 13:00): ')
            consultorio[indice].hora = novo_horario
        case 8:
            nova_especialidade = input('Digite a nova especialidade (ex: cardiologia): ')
            nova_especialidade = nova_especialidade.lower()
            consultorio[indice].especialidade = nova_especialidade
        case 9:
            novo_medico = input('Digite o(a) novo(a) medico(a) (ex: Dra. Cleide Silva): ')
            consultorio[indice].medico = novo_medico
        case 10:
            novo_retorno = input('É um retorno? S para sim e N para nao: ')
            novo_retorno = novo_retorno.upper()
            consultorio[indice].retorno = novo_retorno
        case 0:
            return
        case _:
            print('Opcao invalida! Tente novamente.')
                    

def deletar_paciente(prontuario):
    paciente = buscar_paciente(prontuario)
    if paciente:
                    print(f"""
                      Paciente encontrado:
                      ___________________________________________________________________
                      
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} | IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}
                       ___________________________________________________________________""")
                    deletar = int(input('Tem certeza que deseja deletar? <1-sim / 2-nao>\nN°: '))
                    if deletar == 1:
                        consultorio.remove(paciente)
                        print('Cadastro removido com sucesso!')
                    else:
                        print('Operacao interrompida.')
                        return
    else:
        print('Paciente nao encontrado.')
        return

def exibir_menu():
    print("""
          === CLINICA JOSUE DE CASTRO === 
          
                      MENU
                     ------
                1. Adicionar novo paciente
                2. Buscar paciente
                3. Listar todos os pacientes
                4. Atualizar paciente
                5. Deletar paciente
                0. Sair
                __________________________""")

def main():
    while True:
        #os.system('cls')
        exibir_menu()
        opcao = input("Escolha uma opcao: ")
        
        match opcao:
            case "1":
                #os.system('cls')
                print('\tCADASTRO DE PACIENTE:')
                prontuario = input("\nDigite o prontuario do novo paciente: ")
                nome = input("Digite o nome completo do novo paciente (sem acentos): ")
                idade = input("Digite a idade do novo paciente (apenas numeros): ")
                sexo = input("Digite o sexo do novo paciente <M ou F>: ")
                sexo = sexo.upper()
                cpf = input("Digite o CPF do novo paciente (apenas numeros): ")
                data = input("Digite a data da consulta (ex: 08/07/2024): ")
                hora = input("Digite o horario da consulta (ex: 14:00): ")
                especialidade = input("Digite a especialidade medica (ex: cardiologia): ")
                especialidade = especialidade.lower()
                medico = input("Digite o nome do(a) medico(a) (ex: Dra. Cleide Silva): ")
                retorno = input("Esta consulta e um retorno? S para sim, N para nao: ")
                retorno = retorno.upper()
                
                
                adicionar_paciente(prontuario, nome, idade, sexo, cpf, data, hora, especialidade, medico, retorno)
                
                paciente = buscar_paciente(prontuario)
                
                print(f"""
                      Novo paciente cadastrado com sucesso!
                      _____________________________________
                      
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} | IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}""")
                
                #print("\nPressione Enter para continuar...")
                #char = msvcrt.getch()
            case "2":
                #os.system('cls')
                print('\tBUSCAR PACIENTE:\n')
                prontuario = input("Digite o prontuario do paciente: ")
                paciente = buscar_paciente(prontuario)
                if paciente:
                    print(f"""
                      Paciente encontrado:
                      _____________________________________
                      
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} | IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}""")
                    
                    #print("\nPressione Enter para continuar...")
                    #char = msvcrt.getch()
                else:
                    print("Paciente nao encontrado.")
                    #print("\nPressione Enter para continuar...")
                    #char = msvcrt.getch()
            case "3":
                print('\tListagem Geral dos Pacientes')
                print('\t----------------------------')
                total = 0
                for elemento in consultorio:
                    total = total + 1  
                print(f"\tTotal.........{total}")
                total = 0
                for paciente in consultorio:
                    print(f""" 
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} | IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}
                      ______________________________________________________________________
                       """)
                
            case "4":
                #os.system('cls')
                print('\tALTERAR CADASTRO DE PACIENTE:\n')
                prontuario = input("Digite o prontuario do paciente: ")
                paciente = buscar_paciente(prontuario)
                indice = consultorio.index(paciente)
                if paciente:
                    print(f"""
                      Paciente encontrado:
                      ___________________________________________________________________
                      
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} | IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}
                       ___________________________________________________________________""")
                    atributo = int(input("""
                                     O que deseja alterar:
                                     --------------------
                                     1.Prontuario
                                     2.Nome
                                     3.Idade
                                     4.Sexo
                                     5.Cpf
                                     6.Data da consulta
                                     7.Horario da consulta
                                     8.Especialidade
                                     9.Medico(a)
                                     10.Retorno
                                     0.Cancelar atualizacao
                                     --------------------
                                     N°: """))
                    if atributo == 0:
                        print('Atualizacao cancelada!')
                        #print("\nPressione Enter para continuar...")
                        #char = msvcrt.getch()
                    else:
                        atualizar_paciente(atributo, indice)
                        print(f"""
                      Paciente atualizado com sucesso!
                      _____________________________________
                      
                      PRONTUARIO: {paciente.prontuario} | CPF: {paciente.cpf}
                      NOME: {paciente.nome} IDADE: {paciente.idade} | SEXO: {paciente.sexo}
                      DATA DA CONSULTA: {paciente.data} | HORARIO: {paciente.hora}
                      ESPECIALIDADE: {paciente.especialidade} | MEDICO(A): {paciente.medico}
                      RETORNO: {paciente.retorno}""")
                        
                        #print("\nPressione Enter para continuar...")
                        #char = msvcrt.getch()
                        
                else:
                    print("Paciente nao encontrado.")
                    #print("\nPressione Enter para continuar...")
                    #char = msvcrt.getch()
                    return
            case "5":
                #os.system('cls')
                print('\tEXCLUIR CADASTRO DE PACIENTE:\n')
                prontuario = input("Digite o prontuario do paciente: ")
                deletar_paciente(prontuario)
            case "0":
                print("Saindo do programa. Ate logo!")
                break
            case _:
                print("Opcao invalida. Tente novamente.")
                print("\nPressione Enter para continuar...")
                #char = msvcrt.getch()

if __name__ == "__main__":
    main()

