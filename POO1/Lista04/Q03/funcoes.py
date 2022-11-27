class Func:

    def __init__(self, tot_and, capac_elev, andar_at = 0, pess_pres = 0):
        self.__tot_and = tot_and
        self.__capac_elev = capac_elev
        self.__andar_at = andar_at
        self.__pess_pres = pess_pres
    
    @property
    def get_tot_and(self):
        return self.__tot_and
    
    @property
    def get_capac_elev(self):
        return self.__capac_elev
    
    @property
    def get_andar_at(self):
        return self.__andar_at
    
    @get_andar_at.setter
    def set_get_andar_at(self, andar_at):
        self.__andar_at += andar_at

    @property 
    def get_pess_pres(self):
        return self.__pess_pres
    
    @get_pess_pres.setter
    def set_pess_pres(self, pess_pres):
        self.__pess_pres += pess_pres

    def verifica_espaco_entrada(self):
        if (self.get_pess_pres >= self.get_capac_elev):
            return False
        else:
            return True
        
    def verifica_espaco_saida(self):
        if (self.get_pess_pres == 0):
            return False
        else:
            return True
        
    def entra_pessoa(self, qnt):
        self.set_pess_pres = qnt
    
    def sai_pessoa(self, qnt):
        self.set_pess_pres = qnt
        
    def verifica_andar_subida(self):
        if (self.get_andar_at > self.get_capac_elev):
            return False
        else:
            return True
    
    def sobe_andar(self, qnt):
        self.set_get_andar_at = qnt
    
    def verifica_andar_descida(self):
        if (self.get_andar_at == 0):
            return False
        else:
            return True
    
    def desce_andar(self, qnt):
        self.set_get_andar_at = qnt