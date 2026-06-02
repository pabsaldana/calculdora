def sumar():
    print("Sumar")

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

def raiz_cuadrada():
    print("Raíz Cuadrada")
    numero = float(input("Ingrese el número: "))
    
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        resultado = numero ** 0.5
        print(f"La raíz cuadrada de {numero} es: {resultado}")
