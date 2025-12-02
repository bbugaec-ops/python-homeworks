file = open('data_myfile.txt','r')
#print(file.read(10))
#file.close()
for line in file:
    print(line,end="")
file.close()