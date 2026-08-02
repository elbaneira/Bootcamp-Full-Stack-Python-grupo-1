edad = int(input("ingrese su edad: "))

# 1. Adulto Mayor (60 o más)
if edad >= 60:
    print("La persona es Adulto Mayor, paga $2.000")

# 2. ¿Tiene 18 o más? 
# 18 a 59
elif edad >= 18:
    print("La persona es mayor de edad, paga $5.000")

# 3. Si no es ninguna de las anteriores, cae aquí (Menor de 18)
else:
    print("La persona es menor de edad, paga $1.000")
