class aprendiz:
    instituto = "Sena galan"
    curso = "ADSI"

    def __init__(self,  nombre , CC , edad):
        
        self.nombre = nombre
        
        self.CC = CC
        
        self.edad = edad

    def formar(self):
       print("Formo en programacion")
    
    def finalizarFormacion(self):
       print("Finalizo formación en Junio 2020")
    def getnombre(self):
        return self.nombre
    

    def setnombre(self, nombre):
        if isinstance(nombre, int):
            self.nombre = nombre
        else:
            return "ingrese un nombre de la lista"

nuevoAdsi =aprendiz("kuro","185164",19)
print(nuevoAdsi.setnombre("500"))
print(nuevoAdsi.getnombre())
