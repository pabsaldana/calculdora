def sumar():
    print("Sumar")

def restar():
    print("Restar")

def dividir():
    print("Dividir")

def multiplicar():
    print("Multiplicar")
    num1=int(input("ponga el primer numero a multiplicar"))
    num2=int(input("ponga el segundo numero a multiplicar"))
    resultado=num1*num2
    print(f"el resultado es: {resultado}")

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

num1=0
num2=0

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
