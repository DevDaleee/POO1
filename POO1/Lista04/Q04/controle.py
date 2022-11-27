class Tv:
    def __init__(self, canal="1", volume="50"):
        self.canal = canal
        self.volume = volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num > 0 and num <= 150:
                self.__canal = num
            else:
                print("Canal Inválido")

        else:
            print("O canal deve ser apenas números!")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num >= 0 and num <= 100:
                self.__volume = num
            else:
                print("O volume deve ser entre 0 e 100")

        else:
            print("O volume deve ser apenas números!")


    def mudaCanal(self):
        num = input("Mudar para CANAL: ")
        self.canal = num

    def mudaVolume(self):
        num = input("Mudar para VOLUME: ")
        self.volume = num

    def __str__(self):
        return "CANAL: {} \nvolume: {}\n ".format(self.canal, self.volume)
