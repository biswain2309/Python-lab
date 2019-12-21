f = open("text\inputFile.txt",'r')
passFile = open("text\PassFile.txt", 'w')
failFile = open("text\FailFile.txt", 'w')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

f.close()
passFile.close()
failFile.close()
