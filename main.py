from .temperature import Temperature

temperature_type = input("Ingrese el tipo de temperatura Farenheit (1) o Celcius (2): ")
value = input("Ingrese la temperatura: ")

temperature_instance = Temperature(temperature=value, temperature_type=temperature_type)
print(temperature_instance.get_temperature())