print("Welcome to the Grade Sorter App\n")
grd1 = int(input("What is your first grade (0-100):"))
grd2 = int(input("What is your second grade (0-100):"))
grd3 = int(input("What is your third grade (0-100):"))
grd4 = int(input("What is your fourth grade (0-100):"))
list_grades = []
dropped_gr1 = []
list_grades.append(grd1)
list_grades.append(grd2)
list_grades.append(grd3)
list_grades.append(grd4)
print("Your grades are: {}".format(list_grades))
print("Your grades from lowest to highest are: {}".format(sorted(list_grades)))
print("The lowest two grades will now be dropped")
print("Removed grade: {}".format(sorted(list_grades,reverse=True)[3]))
print("Removed grade: {}".format(sorted(list_grades,reverse=True)[2]))
print("Your remaining grades are: {}".format(sorted(list_grades,reverse=True)[0:2]))
print("Nice work! Your highest score is: {}".format(str((sorted(list_grades,reverse=True)[0:1]))))