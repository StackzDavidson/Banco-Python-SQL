import mysql.connector
import sys


class DataBase:
    def __init__(self, mydb):
        self.logado = False
        self.mydb = mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="cadastro"
        )
        cursor = mydb.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS slogin (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), senha VARCHAR(255), saldo FLOAT(25))")

    def registrar(self):
        cursor = self.mydb.cursor()
        usuario_registro = input('Digite um Nome de Usuário: ')
        seleciona_usuario = f"SELECT nome FROM slogin WHERE nome = '{usuario_registro}'"
        cursor.execute(seleciona_usuario)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            print('Usuario já cadastrado no banco de dados')
            sys.exit()
        else:
            senha_db = input(f'Digite uma senha para o Usuário {usuario_registro}: ')
            insere = f"INSERT INTO slogin(nome, senha, saldo)VALUES('{usuario_registro}', '{senha_db}', '{0}')"
            cursor.execute(insere)
            print('Cadastro Efetuado Com Sucesso!')

    def logar(self):
        login = input('Insira seu usuário: ')
        senha = input(f'Bem-Vindo {login} Digite sua senha: ')

        cursor = self.mydb.cursor()
        login = f"SELECT nome, senha FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
        cursor.execute(login)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            print('Login realizado com Sucesso!')
            self.logado = True
        else:
            print('ERRO Usuário ou Senha Incorreto.')
            sys.exit()

    def depositar(self):
        login = input('Insira seu usuário: ')
        senha = input(f'Bem-Vindo {login} Digite sua senha: ')

        cursor = self.mydb.cursor()
        login = f"SELECT nome, senha FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
        cursor.execute(login)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            print('Login realizado com Sucesso!')
            self.logado = True
        else:
            print('ERRO Usuário ou Senha Incorreto.')
            self.logado = False

        cursor = self.mydb.cursor()

        if self.logado:
            try:
                deposito = float(input('Quanto deseja Depositar R$: '))
                nome_deposito = input('Para quem deseja depositar: ')
                atualiza_saldo = f"SELECT nome FROM slogin WHERE nome ='{nome_deposito}'"
                cursor.execute(atualiza_saldo)
                resultado1 = cursor.fetchall()
                if len(resultado1) != 0:
                    depositar1 = f"UPDATE slogin SET saldo = saldo + '{deposito}' WHERE nome = '{nome_deposito}'"
                    cursor.execute(depositar1)
                    print(f'Depósito No Valor de R${deposito:.2f} feito para a conta {nome_deposito} Efetuado com sucesso! ')
                    sys.exit()
                else:
                    print('Erro Usuario não existe')
                    sys.exit()
            except ValueError as error:
                print('Valor Inválido!')
        else:
            pass

    def sacar(self):
        login = input('Insira seu usuário: ')
        senha = input(f'Bem-Vindo {login} Digite sua senha: ')

        cursor = self.mydb.cursor()
        login3 = f"SELECT nome, senha FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
        cursor.execute(login3)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            print('Login realizado com Sucesso!')
            self.logado = True
        else:
            print('ERRO Usuário ou Senha Incorreto.')
            sys.exit()

        try:
            if self.logado:
                saque = float(input('Quanto deseja sacar: '))
                seleciona_saldo = f"SELECT saldo FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
                cursor.execute(seleciona_saldo)
                resultado1 = cursor.fetchall()
                for valores in resultado1:
                    for saldo in valores:
                        if saque > saldo:
                            print('Saldo insuficiente!')
                            sys.exit()
                        if saque <= saldo:
                            retirada = f"UPDATE slogin SET saldo = saldo - '{saque}' WHERE nome = '{login}' AND senha = '{senha}'"
                            cursor.execute(retirada)
                            print(f'Saque no valor de R${saque:.2f} Efetuado com suceso, seu saldo atual é de R${saldo:.2f}')
                        else:
                            pass
        except ValueError as error:
            print('Valor Inválido!')

    def saldo(self):
        login = input('Insira seu usuário: ')
        senha = input(f'Bem-Vindo {login} Digite sua senha: ')

        cursor = self.mydb.cursor()
        login1 = f"SELECT nome, senha FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
        cursor.execute(login1)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            print('Login realizado com Sucesso!')
            self.logado = True
        else:
            print('ERRO Usuário ou Senha Incorreto.')

        try:
            if self.logado:
                mostra_saldo = f"SELECT saldo FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
                cursor.execute(mostra_saldo)
                resultados = cursor.fetchall()
                for valor in resultados:
                    for v1 in valor:
                        print(f'Seu Saldo é de R${v1:.2f}')
                    else:
                        pass
        except ValueError as error:
            print('Valor Inválido!')

    def tranferir(self):
        login = input('Insira seu usuário: ')
        senha = input(f'Bem-Vindo {login} Digite sua senha: ')

        cursor = self.mydb.cursor()
        login1 = f"SELECT nome, senha FROM slogin WHERE nome = '{login}' AND senha = '{senha}'"
        cursor.execute(login1)
        resultado = cursor.fetchall()
        if len(resultado) != 0:
            print('Login realizado com Sucesso!')
            self.logado = True
        else:
            print('ERRO Usuário ou Senha Incorreto.')
            sys.exit()

        try:
            if self.logado:
                trasnferencia = float(input('Quanto deseja tranferir R$: '))
                para = input('Para quem deseja tranferir: ')
                che_saldo = f"SELECT saldo FROM slogin WHERE nome = '{login}'"
                cursor.execute(che_saldo)
                resultados = cursor.fetchall()
                for valor in resultados:
                    for v1 in valor:
                        if trasnferencia > v1:
                            print('Saldo insuficiente')
                            sys.exit()
                        if trasnferencia <= v1:
                            seleciona_conta_saida = f"UPDATE slogin SET saldo = saldo - '{trasnferencia}' WHERE nome = '{login}' AND senha = '{senha}'"
                            seleciona_conta_recebimento = f"UPDATE slogin SET saldo = saldo + {trasnferencia} WHERE nome = '{para}'"
                            cursor.execute(seleciona_conta_saida)
                            cursor.execute(seleciona_conta_recebimento)
                            saldo_restante = f"SELECT saldo FROM slogin WHERE nome = '{login}'"
                            cursor.execute(saldo_restante)
                            resultados1 = cursor.fetchall()
                            for valores in resultados1:
                                for r1 in valores:
                                    print(f'Seu Saldo Após A transferencia é de R${r1:.2f}')
        except ValueError as error:
            print('Valor Invalido')

    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

    def menu(self):
        print(f'{self.GREEN}+-----------------------------------+\n'
              '|              C6 BANK              |\n'        
              '|    [1] LOGAR                      |\n'
              '|    [2] REGISTRAR                  |\n'
              '|    [3] SACAR                      |\n'
              '|    [4] VER SALDO                  |\n'
              '|    [5] TRANSFERIR                 |\n'
              '|    [6] DEPOSITO                   |\n'
              '|              C6 BANK              |\n'
              f'+-----------------------------------+\n{self.RESET}')
        try:
            b = DataBase(mydb='')
            r = int(input('Oque deseja fazer: '))
            if r == 1:
                b.logar()
            if r == 2:
                b.registrar()
            if r == 3:
                b.sacar()
            if r == 4:
                b.saldo()
            if r == 5:
                b.tranferir()
            if r == 6:
                b.depositar()
            else:
                pass
        except ValueError as error:
            print('Opção Inválida!')


while True:
    b = DataBase(mydb='')
    b.menu()
