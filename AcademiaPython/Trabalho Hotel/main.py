from datetime import datetime
from controller import fazerCheckin, fazerCheckout, procurarHospedes, relatorioHospedes

def menu():

    poli ='='*20
    print(f"{poli} HOTEL {poli}")

    agora=datetime.now(tz=None)

    if agora.hour >=5 and agora.hour<13:
        print("Bom dia")
    if agora.hour >=13 and agora.hour<18:
        print("Boa tade")
    else:
        print("Boa noite")

menu==1

while(menu!=0):
    print('-' * 70)
    print("Escolha a opção desejada:\n")
    menu=int(input("1.FazerCheckin\n2.Relatorio hospedes\n3.Procurar hospedes\n4.FazerCheckout\nQual a sua opção? Por favor digite o número correspondente: "))
    print('|')
    print('-' * 70)
    match menu:
        case 1:
            cliente={}
            cliente["nome"]=str(input("Digite o seu nome completo:"))
            cliente["cpf"]=str(input("Digite o número de seu CPF:"))
            cliente["idade"]=str(input("Digite a sua idade:"))
            cliente["telefone"]=str(input("Digite o número de seu telefone:"))
            fazerCheckin(cliente)
        
        case 2:
            relatorioHospedes()
        case 3:
            clienteFind=str(input("Digite o nome desejado:"))
            procurarHospedes(clienteFind)
        case 4:
            clienteFind=str(input("Digite o nome desejado:"))
            fazerCheckout(clienteFind)
  
