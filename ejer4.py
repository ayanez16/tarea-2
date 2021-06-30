#practica
numero = 23
apellido = "Pardo"

print(numero,type(numero))
print(apellido,type(apellido))

def mensaje(msg):
    print(msg)
    
mensaje("mi primer programa")
mensaje("mi segundo programa")

class sintaxis:
    intancia =0
    def __init__(self,dato="llamando al constructor1"):
        self.frase=dato
        sintaxis.intancia = sintaxis.intancia+1
print("sintaxis antes de instancia es:{}".format(sintaxis.instancia))
ejer1=sintaxis()
print("sintaxis de ejer1 es:{}".format(sintaxis.intancia))
ejer2=sintaxis("instancia2")
print(ejer1.frase)
print("sintaxis de ejer2 es:{}".format(sintaxis.intancia))
print("sintaxis nuevamente de ejer1 es:{}".format(sintaxis.intancia))
print(ejer2.frase)
