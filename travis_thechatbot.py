known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My name s Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
#        string = "Hello {}"
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system(y/n)? :").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem! I didnot want to leave you anyway")
    else:
        print("Hmmm I dont think I have met you {}".format(name))
        addme = input("Would you like to be added to the system(y/n) ?:").strip().lower()

        if addme == "y":
            known_users.append(name)
        elif addme == "n":
            print("No worries! See you around")

