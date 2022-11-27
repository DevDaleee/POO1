import os
import pathlib
import datetime
import csv
import sys
import time
from tabulate import tabulate
from validar_Credencias import *

class MainMenu():
    def __init__(self, listaComida, listaBebida, listaServico, listaPriceComida, listaPriceBebida, listaPriceServico, listaOrder):
        self.comida = listaComida
        self.bebida = listaBebida
        self.servico = listaServico
        self.priceComida = listaPriceComida
        self.priceBebida= listaPriceBebida
        self.priceServico = listaPriceServico
        self.order = listaOrder
    
    def displayMainMenu(self): 
        while True:
            os.system('cls')
            print("*" * 30 + "MAIN MENU" + "*" * 30 + "\n"
                        "\t(P) Pedido\n"
                        "\t(C) Carrinho\n"
                        "\t(Pa) Pagamento\n"
                        "\t(S) Sair\n" + 
                        "_" * 70)
            input_1 = str(input("Select Your Choice: ")).upper()
            if input_1 in ['P', 'C', 'PA', 'S']:
                time.sleep(0.5)
                os.system("cls")
                if input_1 == 'P':
                    OrderMenu.displayOrderMenu(self)
                    break
                elif input_1 == 'C':
                    Report.DisplayReport(self)
                    break
                elif input_1 == 'PA':
                    Pagar.displayPagar(self)
                    break
                elif input_1 == 'S':
                    Exit.ExitProgram()
            else:
                print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
                time.sleep(1)
         
class File(MainMenu):
    headerComida    = ["Comida", "Preço"]
    headerBebida    = ["Bebida", "Preço"]
    headerServico   = ["Serviço", "Preço"]
    
    def Comida(self):
        rowID = []; counter = 0
        with open(r"C:/Users/mdcli/Documents/POO_Python/Trabalho_Final/files/listaComidas.csv", mode='r') as fileComidas:
            csv_reader = csv.reader(fileComidas, delimiter=',')
            next(csv_reader, None)
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                self.comida.append(row)
                self.priceComida.append(row[1])
            print(tabulate(self.comida, headers=File.headerComida, tablefmt="pretty", showindex=rowID))
    
    def Bebida(self):
        rowID = []; counter = 0
        with open(r"C:/Users/mdcli/Documents/POO_Python/Trabalho_Final/files/listaBebidas.csv", mode='r') as fileBebidas:
            csv_reader = csv.reader(fileBebidas, delimiter=',')
            next(csv_reader, None) 
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                self.bebida.append(row)
                self.priceBebida.append(row[1])
            print(tabulate(self.bebida, headers=File.headerBebida, tablefmt="pretty", showindex=rowID))
    
    def Servico(self):
        rowID = []; counter = 0
        with open(r"C:/Users/mdcli/Documents/POO_Python/Trabalho_Final/files/listaServicos.csv", mode='r') as fileServicos:
            csv_reader = csv.reader(fileServicos, delimiter=',')
            next(csv_reader, None)
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                self.servico.append(row)
                self.priceServico.append(row[1])
            print(tabulate(self.servico, headers=File.headerServico, tablefmt="pretty", showindex=rowID))
            
class OrderMenu(MainMenu):
    PrecoTotal = []; date = []
    def displayOrderMenu(self): 
        while True:
            time.sleep(1)
            os.system("cls")
            print("*" * 30 + "O que deseja pedir ?" + "*" * 30 + "\n"
                    "\t(C) Comida\n"
                    "\t(B) Bebida\n"
                    "\t(S) Serviço\n"
                    "\t(V) Voltar Ao Menu\n"
                    "\t(E) Exit\n" + 
                    "_" * 70)
            input_1 = str(input("Select Your Choice: ")).upper()
            if input_1 in ['C', 'B' ,'S', 'V', 'E']:
                os.system("cls")
                if   input_1 == 'C':
                    File.Comida(self)
                    OrderMenu.ProcessOrder(self, input_1)
                elif input_1 == 'B':
                    File.Bebida(self)
                    OrderMenu.ProcessOrder(self, input_1)                
                elif input_1 == 'S':
                    File.Servico(self) 
                    OrderMenu.ProcessOrder(self, input_1)                
                elif input_1 == 'V':
                    MainMenu.displayMainMenu(self) 
                    break
                elif input_1 == 'E':
                    Exit.ExitProgram()
            else:
                print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
                
    def ProcessOrder(self, _input_):
        while True:
            OrderMenu.date.extend([str(datetime.datetime.now())[:10]])
            input_1 = int(input("Selecione O que Deseja Pedir: "))
            if _input_ == 'C':
                quant = str(input("Quantidade: "))
                if input_1 >= 1 and input_1 <= len(self.comida):
                    self.comida[input_1-1].extend(quant)
                    self.order.append(self.comida[input_1-1])
                    Pagar.PrecoTotal += float(self.priceComida[input_1-1])
                    OrderMenu.PrecoTotal.extend([float(self.priceComida[input_1-1]) * float(quant)])
                else:
                    print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
            elif _input_ == 'B':
                quant = str(input("Quantidade: "))
                if input_1 >= 1 and input_1 <= len(self.bebida):
                    self.bebida[input_1-1].extend(quant)
                    self.order.append(self.bebida[input_1-1])
                    Pagar.PrecoTotal += float(self.priceBebida[input_1-1])
                    OrderMenu.PrecoTotal.extend([float(self.priceBebida[input_1-1]) * float(quant)])
                else:
                    print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
            elif _input_ == 'S':
                quant = '1'
                if input_1 >= 1 and input_1 <= len(self.servico):
                    self.servico[input_1-1].extend(quant)
                    self.order.append(self.servico[input_1-1])
                    Pagar.PrecoTotal += float(self.priceServico[input_1-1])
                    OrderMenu.PrecoTotal.extend([float(self.priceServico[input_1-1]) * float(quant)])
                else:
                    print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
            else:
                print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
            
            endLoop = str(input("Deseja Pedir Algo Mais (s/n)? ")).upper()
            if endLoop == 'S':
                print()
                continue
            elif endLoop == 'N':
                print("********Pedido Feito Com Sucesso!********")
                break

class Report(MainMenu):
    headerReport   = ["Pedido", "Preço (R$)", "Quantidade"]
    data = []
    def SaveReport(self):
        with open(r"C:/Users/mdcli/Documents/POO_Python/Trabalho_Final/files/report.fsd", mode='a') as fileReport:
            fileReport.write(f"\nDATE: {str(datetime.datetime.now())[:19]} Total: RM {Pagar.PrecoTotal}\n")
            fileReport.write(tabulate(self.order, headers=Report.headerReport, tablefmt="psql", stralign='center'))
            fileReport.write("\n")
            
    def DisplayReport(self):
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        print(tabulate(self.order, headers=Report.headerReport, tablefmt="psql", stralign='center'))
        print("\n (M) Menu           (C) Comprar          (P) Área de Pagamento          (S) Sair\n" + "_" * 72)
        while True:
            input_2 = str(input("Please Select Your Operation: ")).upper()
            if input_2 in ['C', 'M', 'P', 'E']:
                os.system('cls')
                if (input_2 == 'C'):
                    OrderMenu.displayOrderMenu(self)
                    break
                elif (input_2 == 'M'):
                    MainMenu.displayMainMenu(self)
                    break
                elif (input_2 == 'P'):
                    Pagar.displayPagar(self)
                    break
                elif (input_2 == 'S'):
                    Exit.ExitProgram()
            else:
                print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
                
    def Save(self):
        for i in range(0, len(self.order)):
            Report.data.extend([OrderMenu.date[i]])
            Report.data.extend(self.order[i])
            Report.data.extend([OrderMenu.PrecoTotal[i]])
            with open(r"C:/Users/mdcli/Documents/POO_Python/Trabalho_Final/files/listaReport.csv", mode='a', newline='') as fileReport:
                writer = csv.writer(fileReport)
                writer.writerow(Report.data)
            Report.data.clear()
    
class Pagar(MainMenu):
    PrecoTotal = 0
    def displayPagar(self):
        print("*" * 32 + "Área de Pagamento" + "*" * 33 + "\n")
        print(f"Total Price: R${Pagar.PrecoTotal}")
        Pagar.ProcessarPagar(self)
    
    def ProcessarPagar(self):
        print("\n (P) Pagar          (M) Menu           (D) Disistir Da Compra          (S) Sair\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        while True:
            if input_1 in ['P', 'M', 'D', 'S']:
                os.system('cls')
                if (input_1 == 'P'):
                    senha = input("[ Senha Obrigatória ]: ")
                    if(val.validar_senha(senha) == True):
                        print()   
                        print("Pago com Sucesso!")
                        Report.SaveReport(self)
                        print(tabulate(self.order, headers=Report.headerReport, tablefmt="psql", stralign='center'))
                        Report.Save(self)
                        break
                    else:
                        print(f"\nErro: Senha Inválida({str(input_1)}). Tente Novamente!")
                elif (input_1 == 'M'):
                    MainMenu.displayMainMenu(self)
                elif (input_1 == 'D'):
                    Report.DisplayReport()
                elif (input_1 == 'S'):
                    Exit.ExitProgram()
            else:
                print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")

class HistoricoPedidos():
    def displayHPedidos():
        os.system('cls')
        print("*" * 30 + "Histórico de Compras" + "*" * 30 + "\n")
        rowID = []; counter = 0; data = []; headers = ["Data","Item","Preço(R$)","Quantidade","Valor Total"]
        with open(r"C:/Users/mdcli/Documents/POO_Python/Trabalho_Final/files/listaReport.csv", mode='r') as fileSales:
            csv_reader = csv.reader(fileSales, delimiter=',')
            next(csv_reader, None)
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                data.append(row)
            print(tabulate(data, headers=headers, tablefmt="pretty", showindex=rowID))
                    
class Exit():
    def ExitProgram():
        print("*" * 32 + "Obrigado por usar nosso sistema" + "*" * 31 + "\n")
        sys.exit()
    
listaComida    = []; listaPriceComida     = []
listaBebida   = []; listaPriceBebida    = []
listaServico = []; listaPriceServico  = []
listaOrder   = []
mainMenu = MainMenu(listaComida, listaBebida, listaServico, listaPriceComida, listaPriceBebida, listaPriceServico, listaOrder)

while True:
    os.system('cls')
   
    val = Validar()
    path = pathlib.Path(__file__).parent.absolute()
    path = os.path.join(path, 'senha.json')
    
    if not os.path.isfile(path):
        print("*" * 30 + "Miau Lanches" + "*" * 30 + "\n")
        print(" " * 30 + "Seja Bem-Vindo" + " " * 30 + "\n")
        senha = input("Primeiro Cadastre uma Senha: ")
        val.criar_arq_senhas(senha)   
    
    print("*" * 30 + "Miau Lanches" + "*" * 30 + "\n"
        "\t(H) Histórico de Pedidos\n",
        "\t(C) Comprar\n",
        "_" * 70)
    input_1 = str(input("Digite a sua escolha: ")).upper()
    if input_1 == 'H':
        HistoricoPedidos.displayHPedidos()
        break
    elif input_1 == 'C':
        mainMenu.displayMainMenu() 
        break
    else:
        print(f"\nErro: Valor Inválido({str(input_1)}). Tente Novamente!")
