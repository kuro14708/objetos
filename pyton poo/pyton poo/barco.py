class  barco:
    clase = "comercial"
    compañia = "CFM"

    def __init__(self , capitan , navio , ultimoPuerto):
        self.capitan = capitan
        self.navio = navio
        self.ultimoPuerto = ultimoPuerto

    def getcapitan(self):
     return self.capitan
    

    def setcapitan(self, capitan):
        if isinstance(capitan, int):
            self.capitan= capitan
        else:
            return "ingrese un nombre de la lista"

nuevaFlota = barco("kuro","185164","tokio")
print(nuevaFlota.setcapitan("500"))
print(nuevaFlota.getcapitan())
