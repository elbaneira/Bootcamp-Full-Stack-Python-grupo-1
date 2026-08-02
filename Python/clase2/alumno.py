# Los datos son textos ( input normal)
usuario_ingresado = input("Ingrese su nombre de usuario: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

# La primera entrada (Validar el usuario)
if usuario_ingresado == "alumno":
    
    # --- ¡ESTAMOS ADENTRO DEL PRIMER IF! ---
    # Si el usuario es correcto, se abre la segunda entrada:
    if contrasena_ingresada == "python123":
        print("Acceso permitido")
    else:
        print("Contraseña incorrecta")
    # ---------------------------------------

else:
    # Este 'else' está alineado con el primer 'if'.
    # Significa: ¿Qué pasa si el usuario NO era "alumno"?
    print("Usuario no registrado")