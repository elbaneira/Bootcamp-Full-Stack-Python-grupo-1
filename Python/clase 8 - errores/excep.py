try:
  lista = [10,20,30,50,70,90]
  
  indice = int(input("Ingrese índice: "))
  divisor = int(input("Ingrese divisor: "))
  
  valor = lista[indice]
  resultado = valor /divisor
  
  print("Resultado:", resultado)
  
except ValueError:
  print("Debes ingresar números válidos")
except IndexError:
  print("Índice fuera de rango")
except ZeroDivisionError:
  print("No se puede dividor por cero")
  
finally:
  print("Gracias por participar.")