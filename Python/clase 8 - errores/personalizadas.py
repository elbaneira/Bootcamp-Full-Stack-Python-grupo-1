num1 = int(input("Ingrese el primer número : "))
num2 = int(input("Ingrese el segundo número : "))

class DivisorInvalidoError(Exception):
  pass

try:
  
  if num2 <= 0:
    raise DivisorInvalidoError("El dividor debe ser mayor que 0.")
  
  resultado = num1 / num2
  print("El resultado es:", resultado)

except ZeroDivisionError:
  print("División por 0.")
  
except DivisorInvalidoError as e:
  print("Error:", e)
  
else:
  print("Cálculo realizado correctamente")
  
finally:
  print("Fin del proceso")
  