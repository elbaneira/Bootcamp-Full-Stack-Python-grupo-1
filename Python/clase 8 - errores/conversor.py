class DivisionInvalidoError(Exception):
  pass

num1 = 10
num2 = int(input("Ingrese el divisor: "))

try:
  if num2 <= 0:
    raise DivisionInvalidoError("El divisor debe ser mayor que 0")
  
  resultado = num1 / num2
  print("Resultado:", resultado)

except ZeroDivisionError:
    print("No se puede dividir por cero")
    
except DivisionInvalidoError as error:
  print("Error:", error)

else:
    print("Cálculo realizado correctamente")

finally:
    print("Fin del proceso")
    