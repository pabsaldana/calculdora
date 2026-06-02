def sumar():
    print("sumar")
    num1 = float(input("ingresa primer numero que desea sumar:"))
    num2 = float(input("ingresa el segundo numero:"))
    resultado = num1 + num2                      
    print(f"el resultado es {resultado}")

def restar():
    print("Restar")

def dividir():
    print("Dividir")

def multiplicar():
    print("Multiplicar")

def elevar():
    print("Elevar")

def raiz_cuadrada():
    print("Raiz Cuadrada")

print("welcome to my calculator")

print("1) Sumar")
print("2) Restar")
print("3) Dividir")
print("4) Multiplicar")
print("5) Elevar")
print("6) Raiz Cuadrada")
print("0) Salir")

opcion=int(input("Ingrese opcion a trabajar "))
if opcion==1:
    sumar() 
elif opcion==2:
    restar()
elif opcion==3:
    dividir()
elif opcion==4:
    multiplicar()
elif opcion==5:
    elevar()
elif opcion==6:
    raiz_cuadrada()
elif opcion==0:
    print(f"Salir")
else:
    print("Opcion no encontrada")