def Fahrenheit_to_Celcius(degrees):
    return round(float((5 / 9) * (degrees - 32)), 3)

temperature = int(input())

conversion = Fahrenheit_to_Celcius(temperature)

print(temperature, "Fahrenheit", "Equal to", conversion, "Celcius")