print("Welcome to the Multiplication/Exponent Table app")

name = input("Hello, what is your name:")
num = float(input("What number would you like to work with?"))

print("Multiplication table for %s", num)
for i in range(1,10):
    mult = i*num
    print("{} * {} = {}".format(i,num,round(mult,2)))

for i in range(1,10):
    exp = num**i
    print("{} ** {} = {}".format(num,i,round(exp,4)))