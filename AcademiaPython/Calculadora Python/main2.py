continuar_usando = "SIM"

while continuar_usando == "NÃO":
    print("SELECIONE A OPERAÇÃO DESEJADA")
    print("+ para Adição")
    print("- para Subtração")
    print("* para Multiplicação")
    print("/ para Divisão")

operacao = input("\nQual operação você deseja realizar?")

#Adição
if operacao == "+":

 from controller import adicao

n1 = float(input("Digite o primeiro número: "))
n2 = float(input('Digite o segundo número: '))

print("*"*33,"\n")
print("\nA soma entre", n1,"e",n2,"é:", adicao(n1,n2),"\n")
print("*"*33,"\n")
continuar_usando = input("Gostaria de continuar usando? ").upper()

#Subtração
if operacao == "-":

 from controller import subtracao

n3 = float(input("Digite o primeiro número: "))
n4 = float(input('Digite o segundo número: '))

print("*"*33,"\n")
print("\nA subtração entre", n3,"e",n4,"é:", subtracao(n3,n4),"\n")
print("*"*33,"\n")
continuar_usando = input("Gostaria de continuar usando? ").upper()


#Multiplicação
if operacao == "*":

 from controller import multiplicacao

n5 = float(input("Digite o primeiro número: "))
n6 = float(input('Digite o segundo número: '))

print("\nA multiplicação entre", n5,"e",n6,"é:",multiplicacao,"\n")
print("*"*33,"\n")
print(multiplicacao(n5,n6))
continuar_usando = input("Gostaria de continuar usando? ").upper()
print("*"*33,"\n")

#Divisão
if operacao == "/":

 from controller import divisao

n7 = float(input("Digite o primeiro número: "))
n8 = float(input('Digite o segundo número: '))
while n8 == 0:
    print("O segundo valor não pode ser zero!")
    n8 = float(input("\nDigite o segundo valor (diferente de zero):"))
print("\nA Divisão entre", n7,"e",n8,"é:",divisao,"\n")
print("*"*33,"\n")
print(divisao(n7,n8))
continuar_usando = input("Gostaria de continuar usando? ").upper()
print("*"*33,"\n")

