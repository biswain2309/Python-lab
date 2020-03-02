print("Welcome to the Temperature Conversion Program")
tmp = float(input("What is the given temperature in degree fahrenheit?"))

cs = ((tmp - 32) * 5) / 9
kv = ((tmp + 459.67) * 5) / 9

print("Degrees Fahrenheit:", tmp)
print("Degrees Celsius:", round(cs,4))
print("Degrees Kelvin:", round(kv, 4))