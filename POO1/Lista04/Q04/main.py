import time
from controle import Tv

tv01 = Tv()

while True:
    print("\n"*40)
    print(tv01)

    print("Menu")
    print("---------")
    print("1 - Mudar de Canal")
    print("2 - Aumentar/Diminuir Volume")
    print("3 - Desligar")
    print("\n ---------------")
    selec = input("Selecionar:")

    if selec == "1":
        tv01.mudaCanal()

    elif selec == "2":
        tv01.mudaVolume()

    elif selec == "3":
        print("Desligando ...")
        break

    else:
        print("Selecione uma opção válida!")

    time.sleep(2)