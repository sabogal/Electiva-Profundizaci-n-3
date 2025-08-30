def convertir(valor, opcion):
    if opcion == "horas a segundos":
        return valor * 3600
    elif opcion == "segundos a horas":
        return valor / 3600
    else:
        return "Opción no válida"

print("Conversor de horas y segundos")
print("1. Pasar de horas a segundos")
print("2. Pasar de segundos a horas")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    horas = float(input("Ingresa las horas: "))
    resultado = convertir(horas, "horas a segundos")
    print(f"{horas} horas equivalen a {resultado} segundos.")
elif opcion == "2":
    segundos = float(input("Ingresa los segundos: "))
    resultado = convertir(segundos, "segundos a horas")
    print(f"{segundos} segundos equivalen a {resultado} horas.")
else:
    print("Opción no válida. Elige 1 o 2.")
