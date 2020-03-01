print("Welcome to the Letter Counter App")
count=0
strg = str(input("What is your name?"))
print("Hello " + strg + "!" + "\nI will count the number of times that a specific letter occurs in a message.")
msg = str(input("Please enter a message:")).lower()
ltr = str(input("which letter would you like to count?"))

for char in msg:
    if char == ltr:
        count += 1
print(strg + "," + "your message has " + str(count) + " " + ltr + "'s in it.")
