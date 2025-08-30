from long import convertir_medida
from moneda import execute as moneda_execute
from tiempo import execute as tiempo_execute
from temperature import execute as temperature_execute

option = int(input("Seleccione una opción del menú (1: Tiempo, 2: Moneda, 3: Longitud, 4: Temperatura): "))
CONVERT_TYPE = {
    1: tiempo_execute,
    2: moneda_execute,
    3: convertir_medida,
    4: temperature_execute
}

CONVERT_TYPE[option]()  