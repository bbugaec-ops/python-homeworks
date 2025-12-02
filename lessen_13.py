file_name = 'main.txt'

# file = open(file_name,'w')
# file.write("some text")
# file.close()

file = open(file_name,'a')
file.write("some text ")
file.close()

file = open(file_name,'r')
info = file.read()
print(info)
file.close()