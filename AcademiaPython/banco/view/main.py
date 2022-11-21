from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():

    menu = 1
    while (menu!= 0):
            
        menu_inicial = int(input('opção 1 ou opção 2: '))

        match menu_inicial:

            case 1:
                
                menu = int(input('cadastrar 1 ou listar 2 '))
                
                match menu:

                        case 1:
                            pessoaFisica = PessoaFisica()
                            pessoaFisica.titular = str(input('Digite seu nome: '))
                            pessoaFisica.cpf = int(input('Digite seu cpf: '))
                            pessoaFisica.saldo_inicial = float(input("Digite seu saldo: ")) 
                            
                            resp = str(input('Deseja cadastrar segundo titular?  [s/n]'))
                            
                            if resp in "s":
                                pessoaFisica.segundo_titular = str(input('Digite o nome do segundo titular: '))
                     
                                create_psf(pessoaFisica)
                            else:
                                create_psf(pessoaFisica)

                        case 2:
                            read_psf()

            case 2:

                menu = int(input('cadastrar 1 ou listar 2 '))
                
                match menu:
                        case 1:
                            pessoaJuridica = PessoaJuridica()
                            pessoaJuridica.titular = str(input('Digite o nome da empresa: '))
                            pessoaJuridica.cnpj = int(input('Digite seu cnpj: '))
                            pessoaJuridica.saldo_inicial = float(input("Digite seu saldo: ")) 
                            
                            resp = str(input('Deseja cadastrar segundo titular?  [s/n]'))
                            
                            if resp in "s":
                                pessoaJuridica.segundo_titular = str(input('Digite o nome do segundo titular: '))
                     
                                create_pj(pessoaJuridica)
                            else:
                                create_pj(pessoaJuridica)

                                                            
                        case 2:
                            read_pj()


        