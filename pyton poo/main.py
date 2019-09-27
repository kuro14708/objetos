class Adsi:
    #variables o atributos de clase
    centro = "Comercio y Turismo"

    def __init__(self, estudiantes, ficha, ambiente):
        #atributos o variables de instancia
        #pertenecen solo a la instancia
        self.estudiantes = estudiantes
        self.ficha = ficha
        self.ambiente = ambiente
        
    #metodo de la clase Adsi
    def formar(self):
       print("Formo en programacion")
    
    def finalizarFormacion(self):
       print("Finalizo formación en Junio 2020")
    
    def getEstudiantes(self):
        return self.estudiantes
    
    def setEstudiantes(self, estudiantes):
        if isinstance(estudiantes, int):
            self.estudiantes = estudiantes
        else:
            return "Proporcione un valor entero"
        
       
grupoNuevo = Adsi(20, 18545, 17)

print(grupoNuevo.setEstudiantes("500"))
print(grupoNuevo.getEstudiantes())