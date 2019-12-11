films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}
while True:
    choice = input("What film do you want to watch? :").strip().title()
    if choice in films:
        age = int(input("How old are you? :").strip())
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                films[choice][1] -= 1
                print("Enjoy the film!")
            else:
                print("No enough tickets! See you later!")
        else:
            print("You are too young to watch the film!")
    else:
        print("We dont have that film!")