set1 = set()
with open('first.txt') as f:
    for line in f:
        set1.add(line.strip())
print('Processed first.txt')
set2 = set()
with open('second.txt') as f:
    for line in f:
        set2.add(line.strip())
print('Processed second.txt')
with open('final.txt', 'w') as f:
    for line in set1 - set2:
        f.write(line + '\n')

"""file1 = open('first.txt', 'r')
file2 = open('second.txt', 'r')
FO = open('final.txt', 'w')

for line1 in file1:
    for line2 in file2:
        if line1 == line2:
            FO.write("%s\n" %(line1))

FO.close()
file1.close()
file2.close()"""
