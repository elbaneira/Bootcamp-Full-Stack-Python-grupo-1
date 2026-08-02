#1
película = {
    "título": "Proyect Hail Mary",
    "género": "ciencia ficción",
    "duración": "152",
    "año de estreno": "2026",
}
#2
print(película["título"], película["género"], película["duración"], película["año de estreno"])

#3
for clave in película:
    print(clave, ':', película[clave])

#4
    print(len(película))
#5
    print(película.keys())

    print(película.values())

    print(película.items())

    print("año de estreno", película.get("minutos"))

    película.update({"director": "Phil Lord"})
print(película)
#6
película.update({"duración": "154"})
print(película)

#7
película.pop("año de estreno")
print(película)

#8
película.popitem()
print(película)