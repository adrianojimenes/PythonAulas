import os

def fazerCheckin(cliente):
    with open('hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")

def relatorioHospedes():
    with open('hotel.txt') as arquivo:
        print(arquivo.read())

def procurarHospedes(clienteFind):
    index=0
    flag=0
    arquivo = open("hotel.txt", "r")

    for line in arquivo:
        index +=1
        if clienteFind == eval(line)["nome"]:
            print(line)
            flag =1
    if flag == 0:
        print("Cliente não encontrado")
    arquivo.close()

def fazerCheckout(clienteFind):

    index=0
    flag=0
    arquivo = open("hotel.txt","r")

    for line in arquivo:
        index +=1
        if clienteFind == eval(line)["nome"]:
            chave = index
            flag =1
    if flag == 0:
        print("Cliente não encontrado")
        arquivo.close()
    
        
    try:
        with open ('hotel.txt','r') as fr:

            lines = fr.readlines()

            ptr = 1
        with open ('hotel.txt','w') as fw:
            for line in lines:
                if ptr != chave:
                    fw.write(line)
                ptr += 1
        print("Apagado")
    except:
        print("Algo está errado")