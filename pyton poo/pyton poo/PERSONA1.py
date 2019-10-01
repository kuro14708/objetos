class   persona:

    nacionalidad = "colombianio"
     raza = "humano"

    def __init__(self, nombre , edad , cc):

        self.nombre = nombre
        
        self.cc = cc
        
        self.edad = edad

    def estudio(self):
       print("Formacion en programacion")
    
    def fechaNacimiento(self):
       print("nacio en Junio 1987")

    def getnombre(self):
        return self.nombre
    

    def setnombre(self, nombre):
        if isinstance(nombre, int):
            self.nombre = nombre
        else:
            return "la persona no esta registrada"

nuevoAdsi =persona("kuro","185164",19)
print(nuevoAdsi.setnombre("500"))
print(nuevoAdsi.getnombre())
