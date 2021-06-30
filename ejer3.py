#Funcion For range
frase= input("mi mundo")
for indice in range (len(frase)):
    print(indice,"=", frase [indice])
    
#For in cadena, tupla, lista
cvoc=0
frase= input("ingrese una frase:")
for car in ("a","e","i","o","u","A","E","I","O","U"):
    if car in ["A","E","I","O","U"]:
        continue
    else:
        cvoc = cvoc + 1
print("""cantidad vocales:{}""".format(cvoc))

#comprension- for in datos condicion
[car for car in ["a","e","i","o","u"]if car not in ("a","i","o")]