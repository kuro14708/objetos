class Matematicas:

    def promedioTresNumeros(self, num1, num2, num3):
        pro = (num1 + num2 + num3) / 3
        return pro
    
math = Matematicas()
print(math.promedioTresNumeros(5, 5, 5))