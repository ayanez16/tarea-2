class Ejercicios:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero %2 == 0
        print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))
            
    def perfecto(self,numero):
        acu=0
        for i in range(1, numero):
            if numero % i==0:
                acu=acu+i 
                if numero==acu:
                    print("{}es perfecto".format(numero))
                else:
                    print("{} no es perfecto".format(numero))
                    
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero %i==0
            acu=acu+i
            return acu
        
    def divisores(self,num):
        cont=1
        divisores=[]
        while cont<num:
            rec=num%cont
            if rec == 0
            divisores.append(cont)
            cont = cont+1
            print(divisores)
            
        #Ejercicio de Herencia
class Programacion(Ejercicios):
    def __init__(self):
        pass
    
#prog1_programacion()
#num=28
#acumdivisor=prog1.perfecto2(num)
#if acumdivisor == num
# print(num,"Es perfecto")
#else:
# print(num,"No es perfecto")
#numeros=[3,6,24,28]
#perfectos=[]
#for numero in numeros:
# if prog1.perfecto2(numero)==numero:
# perfectos.append(numero)
#print(perfectos)

def divisores(self,num):
    cont=1
    divisores=[]
    for cont in range(1,num):
        rec=num%cont
        if rec == 0:
            divisores.append(cont)
            return divisores
        
        
prog1 = Programacion()
#print(prog1.divisores(6))
print1=Programacion()
div = prog1.divisores(6)
lista=[1,2]
lista2 = lista+div
print(lista2)




#ejer=Ejercicios()
#num=int(input("ingrese un numero:"))
#print("llamada1")
#resp = ejer.perfecto2(num)
#if numero == resp:
# print("{} es perfecto".format(numero))
# else:
# print("{} no es perfecto".format(numero))
#input()
#lista=[3,5,6,8,28]
#print("llamada2")
#perfectos=[]
#for num in lista:
# if ejer.perfecto2(num)==num:
# perfectos.append(num)
#print(perfectos)

