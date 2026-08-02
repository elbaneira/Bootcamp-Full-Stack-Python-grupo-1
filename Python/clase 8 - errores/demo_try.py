try:
    edad= int(input("Ingrese su edad : "))
    print(f"Su edad es {edad} años")

except ValueError:
    print("Error: debe ingresar un número entero")

try:
    número = int(input("Ingrese un número entero : "))
    print(f"El número ingresado es: {número} ")

except ValueError:
    print("Error: debe ingresar un número entero validado")