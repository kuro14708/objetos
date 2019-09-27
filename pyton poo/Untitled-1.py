class Adsi:
    
    centro = "comercio y turismo"
    # atributos o variables
    #pertenecen solo a la instancia 
    def __init__(self, estudiantes, ficha, ambiente):
            self.estudiantes = estudiantes
            self.ficha = ficha
            self.ambiente = ambiente

    #metodo de la clase Adsi

    def formar(self):
        print("formo en programacion")

    def finalizarFormacion(self):
        print("finalizo formacion en junio 20")

    def getEstudiantes(self):
        return self.estudiantes

    def setEstudiantes(self,estudiantes):
        if isinstance(estudiantes, int):
            self.estudiantes = estudiantes
        else:
            return "Proporcione un valor entero"

grupoNuevo =Adsi(20 , 18545 , 17 )
print(grupoNuevo.formar())
print(grupoNuevo.finalizarFormacion())