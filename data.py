# sistema para entrada da saturação onde o alarme devera ser ativado
# ------------------------------------------------------------------

import pandas as pd
import sys

# Area de definição de funçoes

    
def cadastro():
    Name = input('Nome paciente: ')
    Age = input('Idade paciente: ')
    Sat = input('Saturação indicada: ')


    info_Patients = [
        {'name': Name,
        'idade': Age,
        'saturacao': Sat}]
    
    patients.append(info_Patients)
    
    table = pd.DataFrame(patients)
    table.to_string('my_file.txt',index = False)
    print('\n') 
    print('**informaçoes registradas com sucesso**')
    print('\n') 
  

def DR_only():
    OPT = int(input('[1] Mostrar dados dos pacientes\n[2]Voltar para o menu principal'))
    match OPT:
        case 1:
            CRM = input("CRM:")
            list_CRM.append(CRM)
            print(patients)
        case 2:
            MENU

def linhaMenu():
    print('-'*38)

list_CRM = []
patients = []

# MENU
MENU = True
while MENU:
    linhaMenu()
    print('  **REALIZAR CADASTRO DO PACIENTE**')
    linhaMenu()
    
    OPT = int(input('  [1]PARA CADASTRAR SEUS DADOS\n  [2]CHECAR INFO. PACIENTES(medicos)\n[3]PARA ENCERRAR O PROGRAMA'))
    linhaMenu()
    
    match OPT:
        case 1:
            cadastro()
        case 2:
            DR_only()
        case 3:
            sys.exit()


# o codigo desenvolvido acima é uma parte crucial do sistema sendo desenvolvido
# que no produto final devera ser incorporado com o sistema servindo como a entrada dos dados de cada usuario
# e a base de dados para os medicos