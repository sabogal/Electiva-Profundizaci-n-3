def convertir_medida():
    print("Conversor de medidas 📏")
    print("1. Metros a kilómetros")
    print("2. Kilómetros a metros")
    
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == "1":
        metros = float(input("Ingresa la cantidad en metros: "))
        kilometros = metros / 1000
        print(f"{metros} metros son {kilometros} kilómetros.")
    elif opcion == "2":
        kilometros = float(input("Ingresa la cantidad en kilómetros: "))
        metros = kilometros * 1000
        print(f"{kilometros} kilómetros son {metros} metros.")
    else:
        print("Opción no válida. Por favor elige 1 o 2.")

