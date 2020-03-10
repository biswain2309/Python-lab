class teacher():
    def add_new(self):
        print("\nYour favourite teachers ranked are: {}".format(lst))
        print("Your favourite teachers alphabetically are: {}".format(sorted(lst)))
        print("Your favourite teachers in reverse alphabetical order are: {}\n".format(sorted(lst,reverse=True)))
        print("Your top two teachers are: {} and {}".format(lst[0],lst[1]))
        print("Your next two favourite teachers are: {} and {}".format(lst[2],lst[3]))
        print("Your last favourite teacher is: {}".format(lst[3]))
        print("You have a total of {} teachers\n".format(len(lst)))
    
print("Welcome to favourite teachers Program\n")
global lst
lst=[]
for i in range(4):
    t = str(input("Who is your favourite teacher: "))
    lst.append(t)
new = teacher()
new.add_new()
print("Oops! {} is no longer your first favourite teacher.".format(lst[0]))
l = str(input("Who is your new favourite teacher:"))
lst.insert(0,l)
new.add_new()

