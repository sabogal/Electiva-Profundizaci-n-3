def convertir_moneda(valor, de_moneda, a_moneda):
    # Tasas de conversión simuladas
    tasas = {
        'USD': {'COP': 4000},
        'COP': {'USD': 1 / 4000},
    }

    try:
        tasa = tasas[de_moneda.upper()][a_moneda.upper()]
        return round(valor * tasa, 2)
    except KeyError:
        raise ValueError(f"No se puede convertir de {de_moneda} a {a_moneda}")


# Bloque ejecutable en consola
def execute():
    try:
        valor = float(input("Ingrese el valor a convertir: "))
        de_moneda = input("Ingrese la moneda de origen (USD o COP): ").upper()
        a_moneda = input("Ingrese la moneda destino (USD o COP): ").upper()

        resultado = convertir_moneda(valor, de_moneda, a_moneda)
        print(f"{valor} {de_moneda} equivale a {resultado} {a_moneda}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")