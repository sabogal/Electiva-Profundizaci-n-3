
class Temperature:
	
	def __init__(self, temperature: float, temperature_type: int):
		self.temperature = temperature
		self.temperature_type = temperature_type
	
	def __get_temperature_type(self):
		return {
			1: self.celsius_to_fahrenheit,
			2: self.fahrenheit_to_celsius
		}.get(
			self.temperature_type,
			lambda: (_ for _ in ()).throw(ValueError("Error: Tipo de temperatura no válido."))
		)
	
	def celsius_to_fahrenheit(self):
		return f"Se ha convertido de Celsius a Fahrengeit: {(self.temperature * 1.8) + 32}"
	
	def fahrenheit_to_celsius(self):
		return f"Se ha convertido de Fahrengeit a Celsius: {(self.temperature - 32) / 1.8}"
	
	def get_temperature(self):
		temperature = self.__get_temperature_type()
		return temperature()
	

def execute():

	temperature_type = int(input("Ingrese el tipo de temperatura Farenheit (1) o Celcius (2): "))
	value = float(input("Ingrese la temperatura: "))

	temperature_instance = Temperature(temperature=value, temperature_type=temperature_type)
	try:
		print(temperature_instance.get_temperature())
	except ValueError as e:
		print(e)