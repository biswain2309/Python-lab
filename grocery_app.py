from datetime import datetime

today = datetime.today()
now = datetime.now()

print("Welcome to the Grocery List App")
print("Current Date and Time: {} {}".format(today.strftime("%m/%d"),now.strftime("%H:%M")))

lst = ["Meat", "Cheese"]
print("You currently have {} and {} in your list.".format(lst[0],lst[1]))

for i in range(3):
    item = str(input("Type of food to add to the grocery list: ")).title()
    lst.append(item)
print("Here is your grocery list: {}".format(lst))
print("Here is your grocery list sorted: {}".format(sorted(lst)))
print("\nSimulated grocery shopping..\n")
print("Current grocery list : {} \n{}".format(len(lst),sorted(lst)))
for time in range(len(lst) - 2):
    dela = str(input("What food did you just buy: ")).title()
    for i in range(len(lst)):
        if lst[i] == dela:
            print("Removing {} from the list...".format(dela))
            lst.pop(i)
            break
    print("Current grocery list {} \n{}".format(len(lst),sorted(lst)))
