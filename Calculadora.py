
def sumar():
    print("Sumar")

def restar():
    print("Restar")

def dividir():
    num1=float(input("Ingrese el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))
    resultado=num1/num2
    print(f"El resultado es: {resultado}")

def multiplicar():
    print("Multiplicar")

def elevar():
    base = float(input("ingrese la base: "))
    exponente = float(input("ingrese el exponente: "))
    resultado = base ** exponente
    print("El resultado es:", resultado)

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
while True:
    try:
        opcion = int(input("Ingrese opcion a trabajar "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        dividir()
    elif opcion == 4:
        multiplicar()
    elif opcion == 5:
        elevar()
    elif opcion == 6:
        raiz_cuadrada()
    elif opcion == 0:
        print("Salir")
        break
    else:
        print("Opcion no encontrada")