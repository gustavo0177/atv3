class Temperatura:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

temp = Temperatura()
print(f"25°C em Fahrenheit: {temp.celsius_para_fahrenheit(25):.2f}°F")
